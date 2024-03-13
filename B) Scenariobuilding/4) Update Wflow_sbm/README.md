# 4) Update Wflow_sbm

The corresponding Notebook updates the Wflow_sbm parameterset for the adjusted land cover map. Before running the Notebook, the following steps has to be executed.

## Step 1: Create scenario parameterset

First, you need to copy the original parameterset and rename the Wflow_sbm model to your scenario name. This prevents to adjust the original Wflow_sbm parameterset. 

## Step 2: Create data catalog yaml file

The goal of this data catalog is to provide simple and standardized access to (large) datasets. More information can be found here: https://deltares.github.io/hydromt/latest/user_guide/data_overview.html

In this case, each scenario has a different data catalog file. Herein, the crs, datatype, driver, filesystem, path and nodata value have to be defined. An example:

![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/9b279467-485f-4cbb-9728-1965864b0c37)
