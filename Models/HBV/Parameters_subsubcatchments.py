import pandas as pd
import numpy as np

class Parameters_subsubcatchments(object):
    
    def __init__(self, laterals,
                 Par_Meerssen,S_Meerssen,
                 Par_Sippenaeken,S_Sippenaeken,
                 Par_Hommerich,S_Hommerich,
                 Par_Selzerbeek,S_Selzerbeek,
                 Par_Gulp,S_Gulp,
                 Par_Eyserbeek,S_Eyserbeek):
        
        if type(laterals) == str:
            self._laterals = pd.read_csv(laterals, index_col=[0])
        else:
            print('Incorrect forcing data provided')

        parameter_mapping = {
            'Meerssen': (Par_Meerssen, S_Meerssen),
            'Sippenaeken': (Par_Sippenaeken, S_Sippenaeken),
            'Hommerich': (Par_Hommerich, S_Hommerich),
            'Selzerbeek': (Par_Selzerbeek, S_Selzerbeek),
            'Gulp': (Par_Gulp, S_Gulp), 
            'Eyserbeek': (Par_Eyserbeek, S_Eyserbeek)
            }

        for i, row in self._laterals.iterrows():
            subcatchment_name = row['subcatchment']
            if subcatchment_name in parameter_mapping:
                parameters, s_values = parameter_mapping[subcatchment_name]
                self._laterals.loc[i, ['Imax', 'Ce', 'Sumax', 'beta', 'Pmax', 'Tlag', 'Kf', 'Ks']] = parameters
                self._laterals.loc[i, ['Si', 'Su', 'Sf', 'Ss']] = s_values
                
    @property
    def lateral_id(self):
        #return lateral id's
        return self._laterals.id