import numpy as np
import pandas as pd

from Parameters_subsubcatchments import Parameters_subsubcatchments
from Run_subsubcatchments import Subsubcatchments

class Calibration_subsubcatchments(object):
    
    def __init__(self,Parmin,Parmax,Sin,laterals,forcing,nmax,outdir):
        
        self._Parmin = Parmin
        self._Parmax = Parmax
        self._Sin = Sin
        self._nmax = nmax
        
        for n in range(0, self._nmax):
            Rnum = np.random.random(8)
            
            Par_Meerssen = Rnum * (self._Parmax['Meerssen'] - self._Parmin['Meerssen']) + self._Parmin['Meerssen']
            Par_Sippenaeken = Rnum * (self._Parmax['Sippenaeken'] - self._Parmin['Sippenaeken']) + self._Parmin['Sippenaeken']
            Par_Hommerich = Rnum * (self._Parmax['Hommerich'] - self._Parmin['Hommerich']) + self._Parmin['Hommerich']
            Par_Selzerbeek = Rnum * (self._Parmax['Selzerbeek'] - self._Parmin['Selzerbeek']) + self._Parmin['Selzerbeek']
            Par_Gulp = Rnum * (self._Parmax['Gulp'] - self._Parmin['Gulp']) + self._Parmin['Gulp']
            Par_Eyserbeek = Rnum * (self._Parmax['Eyserbeek'] - self._Parmin['Eyserbeek']) + self._Parmin['Eyserbeek']
            
            S_Meerssen = Sin['Meerssen']
            S_Sippenaeken = Sin['Sippenaeken']
            S_Hommerich = Sin['Hommerich']
            S_Selzerbeek = Sin['Selzerbeek']
            S_Gulp = Sin['Gulp']
            S_Eyserbeek = Sin['Eyserbeek']
        
            par = Parameters_subsubcatchments(laterals,
                                              Par_Meerssen, S_Meerssen,
                                              Par_Sippenaeken, S_Sippenaeken,
                                              Par_Hommerich, S_Hommerich,
                                              Par_Selzerbeek, S_Selzerbeek,
                                              Par_Gulp, S_Gulp,
                                              Par_Eyserbeek, S_Eyserbeek)
            
            run = Subsubcatchments(par, forcing)
            
            run.Q.to_csv(f'{outdir}/run{n+1}.csv')
            par.to_csv(f'{outdir}/run{n+1}.txt')