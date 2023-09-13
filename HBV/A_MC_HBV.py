import numpy       as np
import matplotlib as mpl
from HBVMod import HBVMod
import pandas as pd

forcing=np.genfromtxt('data_WarkEttelbruck_calibration.txt',  dtype=float, autostrip=True)

          #         Imax Ce    Sumax beta   Pmax   Tlag   Kf        Ks
#Calibration step 1
# ParMinn = np.array([0,   0.2,  40,    0.5,   0.001,   0,     0.1,  0.0001])
# ParMaxn = np.array([10,    1,  400,   4,    0.3,     5,    0.5,   0.01])

#Calibration step 2
# ParMinn = np.array([7,   0.5,  200,    3,   0.2,   1,     0.2,  0.0006])
# ParMaxn = np.array([8,    0.7,  250,   4,    0.3,     2,    0.3,   0.01])

#Calibration step 3
Optimum = np.array([7.82581812e+00, 5.86400554e-01, 2.07967771e+02, 3.65392306e+00,
                    2.13464768e-01, 1.68956547e+00, 2.28936235e-01, 9.38878351e-03])
ParMinn = Optimum*0.9
ParMaxn = Optimum*1.1


Sin= np.array([0,  100,  0,  5  ])

forcing= forcing[:,3:6]


# GLUE
nmax=5000
C=np.zeros((nmax,10))
N_feasible = 0

for n in range(1,nmax): 
    Rnum=np.random.random(8) #generate a vector of random number
    Par=Rnum*(ParMaxn-ParMinn)+ParMinn # calculate the random parameter set
    Obj=HBVMod(Par,forcing,Sin,hydrograph='FALSE')[0] #call the model
    Objlog=HBVMod(Par,forcing,Sin,hydrograph='FALSE')[1] #call the model

    if Obj>.6 and Objlog>.6:
        C[N_feasible,0:8]= Par
        C[N_feasible,8]=Obj
        C[N_feasible,9]=Objlog
        N_feasible = N_feasible + 1
    
np.savetxt('test1.txt',C[0:N_feasible,:], delimiter =',')