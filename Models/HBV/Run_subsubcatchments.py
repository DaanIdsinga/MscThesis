import pandas as pd
import numpy as np

from HBVMod_bmi import BmiHBV

class Subsubcatchments(object):
    
    def __init__(self,par,forcing):
        
        laterals = par.lateral_id

        models = []
        simulated_discharge = {}

        for lateral_id in laterals:
            
            model = BmiHBV()
            model.initialize(par,forcing,lateral_id)
            models.append(model)
            new_array = []
            simulated_discharge[lateral_id] = new_array
            
        distant_time = len(forcing.Prec)

        for model in models:
            while model.get_current_time() < distant_time:
            
                model.update()
                simulated_discharge[model.lateral_id].append(model.get_value("Modelled Discharge"))

        for model in models:
            model.finalize()
            
        self._Q = pd.DataFrame(simulated_discharge)
        self._Q.set_index(forcing.Prec.index,inplace=True)
        
        
        # Split Gulp and Sippenaeken equally 
        self._Q['13.001_B_1'] = self._Q['13.001_B']/3
        self._Q['13.001_B_2'] = self._Q['13.001_B']/3
        self._Q['13.001_B_3'] = self._Q['13.001_B']/3

        self._Q['10.001_B_1'] = self._Q['10.001_B']/7
        self._Q['10.001_B_2'] = self._Q['10.001_B']/7
        self._Q['10.001_B_3'] = self._Q['10.001_B']/7
        self._Q['10.001_B_4'] = self._Q['10.001_B']/7
        self._Q['10.001_B_5'] = self._Q['10.001_B']/7
        self._Q['10.001_B_6'] = self._Q['10.001_B']/7
        self._Q['10.001_B_7'] = self._Q['10.001_B']/7

        self._Q = self._Q.drop(columns=['10.001_B','13.001_B'])
        
    @property
    def Q(self):
        return self._Q