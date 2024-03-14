# HBV
This folder contains the used semi-distributed HBV model, build by Hrachowitz (2021). 

![HBV](HBV_parameters.png)

The basic modelling interface (bmi) is applied to the semi-distributed HBV model.

The package bmipy is required to run the code, https://github.com/csdms/bmi-python.

## Model

* HBVMod_bmi: The script of the HBV model with bmi. This is the basis of the model runs.
* HBVMod_bmi_rr: The HBV model script extended with the D-RR output in the HBV lag function
* Weigfun: The lag function of the HBV model, which spreads the discharge of Tlag time.

## Scripts
* Calibration: The script is used for the calibration of the HBV model. It calls the HBV model and calculates the NSE value of the simulated run. The script is used in the calibration Notebooks.
* Calibration_rr: The calibration script extended with the D-RR output in the HBV lag function, this requires a different calculation of the NSE values.
* Forcing:
* Parameters:
* Parameters_subsubcatchments:
* Plots:
* Run:
* Run_subsubcatchments:
* Validation:

# References
Hrachowitz, M. (2021). Lecture 2 - Flow Paths 2021. Technical University Delft. Retrieved 13-09-2023, from https://brightspace.tudelft.nl/d2l/le/content/399298/viewContent/2298342/View
