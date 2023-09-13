import numpy as np
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt
from HBVMod import HBVMod

Q = pd.read_csv('Geul_discharges_compilation.csv', index_col = [0], parse_dates=[0]) #read Geul discharge data
Q = Q['10.Q.36'] #Select Meerssen discharge station
Q = Q['2019-01-01':'2021-07-11'] #Select the time period
Q0 = np.array(Q["2019-01-01 08:00:00":])

ds = xr.open_dataset('inmaps-era5-hourly-2019-2021_mak_knmiP.nc')

ds = ds.sel(time=slice("2019-01-01","2021-07-11"))

P = ds.precip
E = ds.pet

P_total = np.array(xr.DataArray.mean(P,dim=["y","x"]))
E_total = np.array(xr.DataArray.mean(E,dim=["y","x"]))

forcing = ((P_total),(E_total))

Par = [2.27, 0.07, 514.39, 0.98, 0.18, 6.03, 0.019, 0.0004]
Sin = np.array([0,  100,  0,  5  ])
area = 338 #km2

Qm, Si, Su, Sf, Ss = HBVMod(Par,forcing,Sin,area)

plt.figure(figsize=(8,4))
plt.plot(np.array(Q["2019-01-01 08:00:00":].index), Q0, label='Recorded')
plt.plot(np.array(Q["2019-01-01 08:00:00":].index), Qm, label='Modelled')
plt.legend()

fig,ax = plt.subplots(2,2)
fig.suptitle('Storages original HBV')
ax[0,0].plot(Si)
ax[0,0].set_title('Si')
ax[0,1].plot(Su)
ax[0,1].set_title('Su')
ax[1,0].plot(Sf)
ax[1,0].set_title('Sf')
ax[1,1].plot(Ss)
ax[1,1].set_title('Ss')
fig.tight_layout()
