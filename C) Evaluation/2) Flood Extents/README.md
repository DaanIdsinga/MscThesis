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

## Step 4: Clip the flood extent shapefile by the subcatchment outline
The flood extent is larger than the subcatchment outline. So, clip the flood extent by the subcatchment with the clip function:

![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/55032bf2-8e00-43de-a87d-e2f1bdcfc1a3)

![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/040a1efb-f449-4e5e-9488-681246c87535)

## Step 5: Clip the land cover map by the flood extent
Clip the land cover map by the flood extent to investigate the land cover types in the flood extent. Use the Clip raster by mask layer function for this:

![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/f8e1cdb8-0cd3-4e3a-b508-af657d9042a6)

![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/b15ed989-a7f9-4d88-8063-3d7b93d669d7)

## Step 6: Calculate the land cover distribution in the flood extent
The distribution of the land cover classes can be estimated in the land cover map of the flood extent. The Zonal Histogram in the Processing Toolbox is used for this:

![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/bad26efe-a908-4349-9490-4f3e30ead804)

The clipped land cover map at Step 5 is the input in Raster layer. The Vector layer containing zones should contain the flood extent shapefile of Step 4. Finally, save the data as a geopackage at the desired location.

![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/0090e593-e1ed-4a92-b1ac-25dd475ad806)

## Step 7: Calculate the area of the flood extent
The area of the flood extent can be calculated by the Open Field Calculator. Select the layer at Step 4 and Toggle editing on. Open the Field Calculator and calculate the area of the flood extent. The result can be seen in the attribute table.

![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/1b72628a-35f1-491f-8de7-bfc99d8fac76)

![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/9d8887f9-a979-4376-b123-84dccb7e665f)

## Step 8: Calculate the area per land cover class in the flood extent
The calculation of the area per land cover class in the flood extent requires more steps. The distribution of the classes is known in Step 6 and the total area of the flood extent is known in Step 7. Combining this, gives the possibility to calculate the area. Use Excel to perform the calculation. In this case, we want to have the area of the urban land cover classes 111 and 112.
