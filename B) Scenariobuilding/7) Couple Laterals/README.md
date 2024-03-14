# 7) Couple laterals

This section gives the steps to couple HBV and Wflow_sbm offline to D-HYDRO. The modelbuilderscript of Hulsman et al. (2023) is used for this. The script transforms a CSV file with the output of the hydrological model to a input file for D-HYDRO. The lateral input of D-HYDRO is defined in a boundary file. This file contains the boundary conditions as water levels, laterals, meteorological data. The following steps need to be done to couple HBV and wflow_sbm to D-HYDRO.

## Step 1: Create a new model folder
First, copy the folder of the original D-HYDRO model. The lateral timeseries is the only thing that changes in the new model. Rename the copied folder to your scenario name or something else. The new lateral timeseries are created with the moderlbuilderscript in the next steps.

## Step 2: Prepare the afvoersituaties file
At the start of the modelbuilderscript at <B><I>Stap 1: Opgeven instellingen script</I></B>, the Afvoersituaties file is defined. This file contains the information about the lateral input. Here the Name, Kind, Patern, Begintime, Endtime, Fase, Roughness, Laterals file, Precipitation file, and Evaporation file are given. A screenshot of the Afvoersituaties file is shown below:
![Afvoersituaties2](https://github.com/DaanIdsinga/MscThesis/assets/144466847/d52f94ca-6659-41a4-9cc7-0475ff4f684f)

## Step 3: Define the lateral file
At <B><I>Stap 2.1: Tijdsinstellingen</I></B>, the Afvoersituaties.csv is loaded and the name of model is given. This should be a name in the index of the Afvoersituaties file.
![Scenario](https://github.com/DaanIdsinga/MscThesis/assets/144466847/28d1d56a-1621-4364-837a-118ecb41efb4)

Next at <B><I>Stap 2.3: Input data</I></B>, the location of the file with the laterals timeseries is defined. For example a Wlow_sbm scenario:
![Load_laterals](https://github.com/DaanIdsinga/MscThesis/assets/144466847/0e8ca63f-6f5e-4c8f-a771-b2b2728f8c6c)

## Step 4: Run the modelbuilderscript
When the laterals are defined, the modelbuilderscript can be run. It creates a new model folder with the name defined in Step 2. In this folder, a folder containing the FM model is created. Herein, the D-HYDRO laterals are defined in the boundaries.bc file. The FM folder looks like:
![boundaries file](https://github.com/DaanIdsinga/MscThesis/assets/144466847/06a42513-eb59-4dc5-8628-6b3974974cc4)

## Step 5: Adjust the laterals
The boundary conditions in your new created model in Step 1 are split into a DFM_boundaryconditions1d.bc file and a DFM_lateral_sources.bc file. These files contain the water level boundary conditions and the laterals.
![lateral_sources](https://github.com/DaanIdsinga/MscThesis/assets/144466847/3c0482ac-55cc-403e-85c1-72982ca0c61f)

Open the created boundaries.bc file of Step 4 and copy the content. The content is paste in your DFM_lateral_sources.bc file. However, as can be seen below, the water level boundary conditions are present. These should be removed and the laterals should remain. This means that all forcings with a constant function are removed from the file. Save the lateral sources file and your new D-HYDRO model is ready to run a scenario.
![boundaries file2](https://github.com/DaanIdsinga/MscThesis/assets/144466847/8e53e0ac-f19d-449c-b66a-72829e8c55fd)

The scenario is ready to run in D-HYDRO!

# References
Hulsman, R., Weijers, L., Verstegen, E., & Goedbloed, A. (2023). Modelbouw D-HYDRO Geul. Royal HaskoningDHV
