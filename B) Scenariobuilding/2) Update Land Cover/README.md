# 2) Update land cover

The scenario idea is translated in a new land cover map, containing the added paved area. Updating the land cover map consists of multiple steps. The software QGIS used for this and the plugin Serval.

## Step 1: Draw the polygons of the new houses in QGIS

### Step 1.1: Create a new shapefile
First, create a new shapefile, wherein the new houses are drawn.
![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/e7ad152b-2644-4be4-9249-0ade8baf31dd)

### Step 1.2: Draw the polygons containing the paved area
In the created shapefile, polygons are added. These polygons represent the new paved areas. Toggle editing on and add a polygon by:
![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/1512c9c2-484f-4a90-82a1-360161daed0f)

Draw polygons for the new paved area in areas without paved areas. Assign to each polygon the subsubcatchment or the corresponding village names. For example Scenario 2b1:
![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/dd249680-7088-4419-90d7-5348dc38a5ed)


[Note]: keep in mind the existing sewerage areas of D-RR. Each polygon with new paved area should have a connection to a sewerage area in D-RR, otherwise the new paved area is not added to the model. 

### Step 1.3: Calculate the total area of the added paved area
Check the total added paved area. When your area is too large, remove some polygons. When your added area is too small, go back to Step 1.2. 

The area is calculated by the Open Field Calculator. Toggle editing on and create a new field, containing the areas:
![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/9a679c37-707c-4489-b8e1-9fe455516c39)

When the required new paved area is drawn, you can proceed to Step 2.

## Step 2: Change the land cover map

### Step 2.1: Install Serval plugin
With the use of this plugin, it is possible to adjust geotiffs.
![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/35769ac1-816e-49cb-8670-bdf3d1f32833)

### Step 2.2: Copy the original land cover map
Copy the original land cover map and rename it to your scenario name. This land cover map will be adjusted.

### Step 2.3: Select your scenario land cover map in Layers
![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/abedb592-6634-4afe-80bf-9923b85c3756)

### Step 2.4: Select your created shapefile
Use Create Selection From Layer to select your shapefile, containing the new paved area.
![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/dfb9d0e2-85fa-49de-8735-a4e83d2ed225)

![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/984531b4-eb55-4712-9b78-aed9267a7121)

### Step 2.5: Adjust the land cover of the selected area
In this case, the new paved area gets the land cover type <I>112: Discontinuous Urban Fabric</I>. So, fill in this land cover type in the Serval bar:
![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/26d93ed0-c019-45e4-9e37-e8c9c0abf4e6)

Next, apply this land cover type to the selected area by Apply Value(s) To Selection:
![image](https://github.com/DaanIdsinga/MscThesis/assets/144466847/f580d2bf-1a4f-4a1e-bb0a-cb23d0016eeb)

It could take some time before the land cover map is adjusted. 
