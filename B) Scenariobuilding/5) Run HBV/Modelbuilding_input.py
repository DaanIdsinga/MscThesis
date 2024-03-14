## Import required packages
import numpy as np
import pandas as pd

## Import required HBV scripts
from Run_subsubcatchments import Subsubcatchments
from Parameters_subsubcatchments import Parameters_subsubcatchments
from Forcing import Forcing

## Define work directory
workdir = r"C:\Users\924259\OneDrive - Royal HaskoningDHV\Documents\Master thesis Daan Idsinga\Modellen\HBV\HBV Kalibratie"

## Define output directory
outdir = r"C:\Users\924259\OneDrive - Royal HaskoningDHV\Documents\Master thesis Daan Idsinga\Modellen\Modelbouw_input\HBV"

## Define the updated unpaved areas of the laterals
laterals = r"C:\Users\924259\OneDrive - Royal HaskoningDHV\Documents\Master thesis Daan Idsinga\Modellen\Scenarios\Laterals\laterals_scenario3e3.txt"

## Define the parameters per subcatchment
Par_Meerssen =      np.array([1.78,	0.276,	276.4,	7.52,	0.0678,	33.4,	0.0643,	0.0450])
Par_Hommerich =     np.array([1.28,	0.905,	794.0,	7.28,	0.512,	9.51,	0.0942,	0.0321])
Par_Gulp =          np.array([2.02,	0.747,	631.7,	5.23,	0.0483,	6.39,	0.0438,	0.00394])
Par_Eyserbeek =     np.array([1.24,	0.995,	922.5,	6.14,	0.0140,	5.05,	0.0954,	0.00330])
Par_Selzerbeek =    np.array([1.12,	0.412,	703.6,	4.20,	0.0298,	10.6,	0.0622,	0.00221])
Par_Sippenaeken =   np.array([1.17,	0.609,	274.4,	2.64,	0.0347,	7.75,	0.0398,	0.0196])

## Define the initial storages
S_Meerssen = S_Sippenaeken = S_Hommerich = S_Selzerbeek = S_Gulp = S_Eyserbeek = np.array([0,10,0,5])

## Define the forcing
forcing = Forcing(f'{workdir}\Forcing/validation_precipitation_subsubmean.csv',
                                   f'{workdir}\Forcing\Val_Evaporation.csv',
                                   )

## Create the parameterset
par = Parameters_subsubcatchments(laterals,
                                  Par_Meerssen, S_Meerssen,
                                  Par_Sippenaeken, S_Sippenaeken,
                                  Par_Hommerich, S_Hommerich,
                                  Par_Selzerbeek, S_Selzerbeek,
                                  Par_Gulp, S_Gulp,
                                  Par_Eyserbeek, S_Eyserbeek)

## Run HBV for each subsubcatchment
Run = Subsubcatchments(par, forcing)

## Save the output per lateral to a csv file
Run.Q.to_csv(f'{outdir}/scenario3e3_HBV.csv')
