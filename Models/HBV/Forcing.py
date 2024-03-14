import pandas as pd
import numpy as np

class Forcing(object):
    
    def __init__(self, Prec, Evap, subcatchment=0):
            
        if subcatchment == 0:
                
            if type(Prec) == str:
                self._Prec = pd.read_csv(Prec,index_col=[0],parse_dates=[0])
            else:
                print('Incorrect forcing data provided')
                    
        elif type(subcatchment) == str:
                
            if type(Prec) == str:
                self._Prec = pd.read_csv(Prec,index_col=[0],parse_dates=[0])
                self._Prec = self._Prec[f'{subcatchment}']
            else:
                print('Incorrect forcing data provided')
                
        else:
            print('Incorrect subcatchment is provided')
                        
        if type(Evap) == str:
            self._Evap = pd.read_csv(Evap,index_col=[0],parse_dates=[0])
        elif np.issubdtype(Evap.dtype, np.floating):
            self._Evap = Evap
        else:
            print('Incorrect forcing data provided')
            
    @property
    def Prec(self):
        #Set precipitation
        return self._Prec
    
    @property
    def Evap(self):
        #Set evaporation
        return self._Evap