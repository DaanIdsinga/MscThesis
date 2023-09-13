# HBV basis model
This folder contains the basis of the semi-distributed HBV model. The basic modelling interface (bmi) is applied to this model.

## Files
- HBVMod.py contains the semi-distributed HBV model for hourly timesteps and returns the modelled discharge
- HBVMod_cal.py can be used for calibrating the HBV model. The function returns the objective and logobjective. These are 1 - Nash-Shutcliff coefficient, for the modelled discharge and the logarithm of the modelled discharge.
- Weighfun.py contains the transformation function of the HBV model. The discharge is spread out of Tlag timesteps. 
- HBV_run.py contains a run of the complete Geul catchment, with calibrated parameters by Thewissen (2022).

# References
