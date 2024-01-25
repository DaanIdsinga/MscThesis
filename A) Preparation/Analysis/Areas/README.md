# Determine Paved and Unpaved Areas

The data of the sewerage areas and the definition of the subsubcatchments are retrieved from the Waterboard of Limburg. The sewerage areas are connected to a sewer, which is connected to the Geul river by a sewer overflow. When a sewer is full, the excess water flows via the sewer overflow in the Geul. Each sewerage area consists of paved and unpaved areas. For each sewerage area, the corresponding paved area is given in the data. However, as can be seen in the figure below, the sewerage areas intersect multiple subsubcatchments, for example in Valkenburg. Analysis is done to calculate the paved and unpaved area per subsubcatchment with a step-by-step plan and the use of the software.

<p align="center">
  <img width="500" src="Paved_areas.png">
</p>

## Step 1: Calculate the areas of the sewerage areas

First the area of each sewerage area is calculated with use of the Open Field Calculator in QGIS. 

## Step 2: Determine the ratios between the paved and sewerage areas

The paved area per sewerage area is kwown. The second step is determining the ratios between the paved and sewerage areas for each polygon. This is done by dividing the sewerage area by the paved area.

## Step 3: Cut the sewerage areas at the boundaries of the subsubcatchments

In the third step, the sewerage areas are cut at the boundaries of the subsubcatchments. This makes it possible to calculate the area of the sewerage areas per subsubcatchment. The following step is executed in QGIS:

<I>Vector > Geoprocessing Tools > Intersection</I>

<I>Input layer: “GEU\_rioleringsgebied"</I>

<I>Overlay layer: "GEU\_HBV\_deelstroomgeb\_Dhydro\_2022\_met\_neerslagregios"</I>

This results in the figure below for the example in Valkenburg. It can be seen that the sewerage areas are split at the boundaries of the subsubcatchments.

<p align="center">
  <img width="500" src="Paved_areas_split.png">
</p>

## Step 4: Calculate the area of each cut sewerage area

In the next step, the area of each split sewerage areas is calculated with the Open Field Calculator in QGIS. This is needed for the next two steps, where the total paved area per subsubcatchment is determined.

It can be seen that there is a difference between the figures. The sewarage areas outside the subsubcatchments are left out and are not considered. These sewerage areas are kept constant during the scenario simulations in this research.

## Step 5: Determine the paved area per cut sewerage area

The paved areas per cut sewerage area are determined by multiplying the sewerage areas by the ratios, determined in Step 3.

## Step 6: Determine the paved area per subsubcatchment

In Step 6, the total paved area per subsubcatchment is determined. This is the sum of the paved areas in a subsubcatchment.

## Step 7: Determine the unpaved area per subsubcatchment

In the last step, the unpaved area of a subsubcatchment is calculated by subtracting the paved area from the total area. The calculated unpaved area becomes the input of the HBV model.

# Determine Adjustment Ratios

The paved and unpaved areas change when a scenario is constructed. It is needed to know which paved D-RR areas will be adjusted when a unpaved HBV area is changed and vice versa. Analysis is done to find the relation between the areas. This results in adjustment ratios, that define how an subsubcatchment area change is translated to the D-RR areas. So, when the paved area in a subsubcatchment is increased, it can be calculated which D-RR areas increase and by how much, with the use of the adjustment ratios. The adjustment ratios are determined in three steps.

## Step 8: Connect the sewerage areas to the sewer overflows

The D-RR laterals are defined as sewer overflows. Each sewer overflow is connected to a paved catchment, which determines the amount flow to the river. The sewer overflows are connected to the sewerage areas by their corresponding area code in this step.

## Step 9: Connect the cut paved areas to the sewer overflows

Next, the cut paved areas, determined in Step 3, are connected to the sewer overflows. This is needed to know which paved catchment in D-RR corresponds to which unpaved HBV subsubcatchment.

A couple of sewerage areas are divided over two or three sewer overflows. A distribution ratio is defined in the data for these sewerage areas. These ratios equally distribute the sewerage area over the sewer overflows.

## Step 10: Calculate adjustment ratios

In the last step, the adjustment ratios are calculated. The ratios are based on how the paved areas are distributed over the subsubcatchments and the D-RR areas. If, for example, a subsubcatchment is connected to three D-RR areas, the adjustment ratio is determined by the distribution of the paved area over these D-RR areas. 
