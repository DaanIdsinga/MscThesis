import pandas as pd
import numpy as np

from HBVMod_bmi import BmiHBV

class Run(object):
    
    def __init__(self,par,forcing,Qobs,Qrr,Qup):
        
        model = BmiHBV()

        model.initialize(par,forcing)

        distant_time = len(Qobs)

        Qmod = []

        while model.get_current_time() < distant_time:
            model.update()
            Qmod.append(model.get_value("Modelled Discharge"))
        
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
        
        
        self._Q = pd.DataFrame()
        self._Q['Qobs'] = Qobs
        self._Q['Qmod'] = Qmod

    @property
    def Q(self):
        return self._Q