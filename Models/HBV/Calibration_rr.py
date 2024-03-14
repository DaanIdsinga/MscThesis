import numpy as np
import pandas as pd

from HBVMod_bmi_rr import BmiHBV
from Parameters import Parameters

class Calibration(object):
    
    def __init__(self,Parmin,Parmax,Sin,area,forcing,Qobs,Qup,Qrr,calperiod,nmax,nse):
        self._Parmin = Parmin
        self._Parmax = Parmax
        self._Qobs = Qobs.values.ravel()
        self._nmax = nmax
        self._C = np.zeros((self._nmax,11))
        self._N = 0
        
        for n in range(0, self._nmax):
            Rnum = np.random.random(8)
            Par = Rnum * (self._Parmax - self._Parmin) + self._Parmin
            
            par = Parameters(Par,Sin,area)
    
            model = BmiHBV()
            model.initialize(par,forcing, Qrr)
            
            distant_time = len(forcing.Prec)
            
            Qmod = []    
            
            while model.get_current_time() < distant_time:
                
                model.update()
                Qmod.append(model.get_value("Modelled Discharge"))
            
            model.finalize()

            if isinstance(Qup, (int, float)) and Qup == 0:
                Qmod = Qmod
            elif isinstance(Qup, (list, np.ndarray)) and (Qup == 0).all():
                Qmod = Qmod
            else:
                Qmod = Qmod + Qup.values.ravel()

            period = [len(Qobs[calperiod[0]:calperiod[1]]) - 1, len(Qobs[calperiod[0]:calperiod[2]])]
            
            Qobs_cal = self._Qobs[period[0]:period[1]]
            Qmod_cal = np.array(Qmod[period[0]:period[1]])
            
            Disch = pd.DataFrame()
            Disch['Qobs'] = Qobs_cal
            Disch['Qmod'] = Qmod_cal
            Disch.index = Qobs[calperiod[1]:calperiod[2]].index
            Cum_Disch = Disch.cumsum()

            ind = np.where((Qobs_cal>=0) & (Qmod_cal>=0))
            QoAv = np.mean(Qobs_cal[ind])
            ErrUp = np.sum((Qmod_cal[ind]-Qobs_cal[ind])**2)
            ErrDo = np.sum((Qobs_cal[ind]-QoAv)**2)
            Obj = 1 - (ErrUp/ErrDo)
            
            QoAv_sum = Cum_Disch['Qobs'].mean()
            ErrUp_sum = np.sum((Cum_Disch['Qmod']-Cum_Disch['Qobs'])**2)
            ErrDo_sum = np.sum((Cum_Disch['Qobs']-QoAv_sum)**2)
            Obj_sum = 1 - (ErrUp_sum/ErrDo_sum)
            
            De = np.sqrt((1-Obj)**2+(1-Obj_sum)**2)

            if Obj > nse and Obj_sum > nse:
                self._C[self._N,0:8] = Par
                self._C[self._N,8] = Obj
                self._C[self._N,9] = Obj_sum
                self._C[self._N,10] = De
                self._N = self._N + 1
                
            print(f"Current n: {n}", end="\r")
        
        self._C = self._C[self._C[:,8]>0]
        
    @property
    def C(self):
        return self._C
    
    @property
    def Q(self):
        return self._Disch
    
    @property
    def Qcum(self):
        return self._Cum_Disch