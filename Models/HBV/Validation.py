import numpy as np
import pandas as pd

from HBVMod_bmi import BmiHBV
from Parameters import Parameters

class Validation(object):
    
    def __init__(self,Optpar,Sin,area,forcing,Qobs,Qup,Qrr,valperiod):
        
        self._Qobs = Qobs.values.ravel()
        
        par = Parameters(Optpar,Sin,area)

        model = BmiHBV()
        model.initialize(par,forcing)
        
        distant_time = len(Qobs)
        
        Qmod = []    
        
        while model.get_current_time() < distant_time:
            
            model.update()
            Qmod.append(model.get_value("Modelled Discharge"))
        
        model.finalize()
        
        if isinstance(Qrr, (int, float)) and Qrr == 0:
            Qmod = Qmod
        elif isinstance(Qrr, (list, np.ndarray)) and (Qrr == 0).all():
            Qmod = Qmod
        else:
            Qmod = Qmod + Qrr.values

        if isinstance(Qup, (int, float)) and Qup == 0:
            Qmod = Qmod
        elif isinstance(Qup, (list, np.ndarray)) and (Qup == 0).all():
            Qmod = Qmod
        else:
            Qmod = Qmod + Qup.values.ravel()
            
        period = [len(Qobs[valperiod[0]:valperiod[1]]) - 1, len(Qobs[valperiod[0]:valperiod[2]])]
         
        Qobs_val = self._Qobs[period[0]:period[1]]
        Qmod_val = np.array(Qmod[period[0]:period[1]])
         
        Disch = pd.DataFrame()
        Disch['Qobs'] = Qobs_val
        Disch['Qmod'] = Qmod_val
        Disch.index = Qobs[valperiod[1]:valperiod[2]].index
        self._Cum_Disch = Disch.cumsum()

        ind = np.where((Qobs_val>=0) & (Qobs_val!=0))
        QoAv = np.mean(Qobs_val[ind])
        ErrUp = np.sum((Qmod_val[ind]-Qobs_val[ind])**2)
        ErrDo = np.sum((Qobs_val[ind]-QoAv)**2)
        self._Obj = 1 - (ErrUp/ErrDo)
         
        QoAv_sum = self._Cum_Disch['Qobs'].mean()
        ErrUp_sum = np.sum((self._Cum_Disch['Qmod']-self._Cum_Disch['Qobs'])**2)
        ErrDo_sum = np.sum((self._Cum_Disch['Qobs']-QoAv_sum)**2)
        self._Obj_sum = 1 - (ErrUp_sum/ErrDo_sum)
         
        self._De = np.sqrt((1-self._Obj)**2+(1-self._Obj_sum)**2)

        self._Disch = pd.DataFrame()
        self._Disch['Qobs'] = self._Qobs
        self._Disch['Qmod'] = Qmod
        self._Disch.index = Qobs[valperiod[0]:valperiod[2]].index
        
    @property
    def Obj(self):
        return self._Obj
    
    @property
    def Obj_sum(self):
        return self._Obj_sum
    
    @property
    def De(self):
        return self._De
    
    @property
    def Q(self):
        return self._Disch
    
    @property
    def Qcum(self):
        return self._Cum_Disch