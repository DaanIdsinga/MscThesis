# Flood extents

This section describes how to analyse the simulated flood extents and to calculate the areas.

## Step 1: Open the results by the DFM_fou.nc file
Start QGIS and open the output DFM_fou.nc file in it. Select the Mesh2d:

![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/1d4323e6-9bc2-4ca1-a665-fb073156df0d)

Next, select the Coordinate Reference System. In this case it is EPSG:28992 Amersfoort/RD new:

![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/6006bfb7-f8c7-405e-9630-d9b6fe183d22)

Right click the added layer and open the properties. Select Symbology and Groups. The variable we want to analyse is <I>Maximum 001: water level, maximum depth value</I>. Click on the square on the right of this variable:

![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/c53b228f-c024-4fad-b93c-8ebf2960ffdd)

Next, go to the contours tab. Here you can adjust the colors of the layer. Select a minimum value of 0.01 meter and check the box of Clip out of range values:

![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/74a0db47-e9c7-40bb-ba50-7e98fe38a078)

Finally, rename the layer to your scenario name and add an Open Street Map as background layer by:

![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/66adf52c-dbe7-46aa-a416-5b03666656e9)

## Step 2: Create flood extent contour layer
To be able to calculate the area of the flood extent, the mesh layer should be converted to a shape layer. The first step is to create a layer containing the contours of the flood extent.

Open the Processing Toolbox and open Mesh > Export contours:

![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/c42e1c86-610d-4fdd-82fa-a1f92074fed8)

Select the mesh layer at Input mesh layer. At Dataset groups, click Current Dataset Group, which contains the maximum depth value. At List of contours level, type 0.01, 8. In this case, one contour is created between the selected minimum of 0.01 meter and a random maximum value outside of the values in the layer. Do not save the contour lines, as they are not used. Save the output as geopackage at the desired location.

![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/8c26a411-4bda-4f22-a288-f66f1e78d93e)

## Step 3: Create flood extent shapefile
The result of the flood extent contour layer is not ready for use, as can be seen:

![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/24ad09bd-43cf-4151-9391-31950b4e9de3)

The contour layer will be fixed by the function 'Buffer', which can be found in the Processing Toolbox: Vector geometry > Buffer:

![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/151dcc2a-6f51-4c57-9a3f-ef6e8bb92efd)

Enter the contour layer at Input layer. Fill 0.01 at Distance and keep the other values the same. Save the Buffered layer at the desired location.

![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/aa852358-6dbc-4d48-9a72-ecfdd6282b41)

## Step 4: 




