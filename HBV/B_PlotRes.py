import numpy       as np
import matplotlib.pyplot as plt
from HBVMod import HBVMod
import pandas as pd

forcing=np.genfromtxt('data_WarkEttelbruck_calibration.txt',  dtype=float, autostrip=True)

Sin= np.array([0,  100,  0,  5  ])

forcing= forcing[:,3:6]

x=pd.read_csv('test1.txt',delimiter=',',header=None)

plt.figure(1)
plt.plot(x[9],x[8], '.')
plt.xlabel('NSE log(Q)')
plt.ylabel('NSE (Q)')
optimum=(x[8]+x[9]).idxmax()
OptPar=np.array(x.loc[optimum,0:7])
print(f'The maximum calibration N for Q is {max(x[8])}')
print(f'The maximum calibration N for log(Q) is {max(x[9])}')
print(f'The optimum calibration N for Q is {x[8][optimum]} and for log(Q) is {x[9][optimum]}')
print(f'The optimum parameterset is {OptPar}')

plt.figure(2)
plt.title('HBV model calibration')
plt.xlabel('Days')
plt.ylabel('Discharge (mm/day)')
Obj=HBVMod(OptPar,forcing,Sin,hydrograph='True')

plt.figure(3)
plt.suptitle('Q',y = 1.05, fontsize=14, va='center')
plt.subplot(421)
plt.plot(x[0],x[8],'.')
plt.xlabel('Imax')
plt.ylabel('NSE(-)')
plt.xlim(min(x[0]),max(x[0]))

plt.subplot(422)
plt.plot(x[1],x[8],'.')
plt.xlabel('Ce')
plt.xlim(min(x[1]),max(x[1]))

plt.subplot(423)
plt.plot(x[2],x[8],'.')
plt.xlabel('Su,max')
plt.ylabel('NSE(-)')
plt.xlim(min(x[2]),max(x[2]))

plt.subplot(424)
plt.plot(x[3],x[8],'.')
plt.xlabel('Beta')
plt.xlim(min(x[3]),max(x[3]))

plt.subplot(425)
plt.plot(x[4],x[8],'.')
plt.xlabel('Pmax')
plt.ylabel('NSE(-)')
plt.xlim(min(x[4]),max(x[4]))

plt.subplot(426)
plt.plot(x[5],x[8],'.')
plt.xlabel('Tlag')
plt.xlim(min(x[5]),max(x[5]))

plt.subplot(427)
plt.plot(x[6],x[8],'.')
plt.xlabel('Kf')
plt.ylabel('NSE(-)')
plt.xlim(min(x[6]),max(x[6]))

plt.subplot(428)
plt.plot(x[7],x[8],'.')
plt.xlabel('Ks')
plt.xlim(min(x[7]),max(x[7]))

plt.tight_layout()

plt.figure(4)
plt.suptitle('log(Q)',y = 1.05, fontsize=14, va='center')
plt.subplot(421)
plt.plot(x[0],x[9],'.')
plt.xlabel('Imax')
plt.ylabel('NSE(-)')
plt.xlim(min(x[0]),max(x[0]))

plt.subplot(422)
plt.plot(x[1],x[9],'.')
plt.xlabel('Ce')
plt.xlim(min(x[1]),max(x[1]))

plt.subplot(423)
plt.plot(x[2],x[9],'.')
plt.xlabel('Su,max')
plt.ylabel('NSE(-)')
plt.xlim(min(x[2]),max(x[2]))

plt.subplot(424)
plt.plot(x[3],x[9],'.')
plt.xlabel('Beta')
plt.xlim(min(x[3]),max(x[3]))

plt.subplot(425)
plt.plot(x[4],x[9],'.')
plt.xlabel('Pmax')
plt.ylabel('NSE(-)')
plt.xlim(min(x[4]),max(x[4]))

plt.subplot(426)
plt.plot(x[5],x[9],'.')
plt.xlabel('Tlag')
plt.xlim(min(x[5]),max(x[5]))

plt.subplot(427)
plt.plot(x[6],x[9],'.')
plt.xlabel('Kf')
plt.ylabel('NSE(-)')
plt.xlim(min(x[6]),max(x[6]))

plt.subplot(428)
plt.plot(x[7],x[9],'.')
plt.xlabel('Ks')
plt.xlim(min(x[7]),max(x[7]))

plt.tight_layout()
plt.show()

forcing=np.genfromtxt('data_WarkEttelbruck_validation.txt',  dtype=float, autostrip=True)

Sin= np.array([0,  100,  0,  5  ])
forcing= forcing[:,3:6]
Obj=HBVMod(OptPar,forcing,Sin,hydrograph='FALSE')[0] #call the model
Objlog=HBVMod(OptPar,forcing,Sin,hydrograph='FALSE')[1] #call the model
print(f'The validation N for Q is {Obj}')
print(f'The validation N for log(Q) is {Objlog}')

plt.figure(5)
plt.title('HBV model validation')
plt.xlabel('Days')
plt.ylabel('Discharge (mm/day)')
Q=HBVMod(OptPar,forcing,Sin,hydrograph='True')