# Forcing Processing

This part describes how the forcing is processed. The following datasets are processed:

* ERA5-Land Potential Evaporation and Temperature: Process the data and reproject the coordinates to the Wflow_sbm Geul parameterset coordinates;
* ERA5-Land Total Evaporation: Process the data and create NetCDF file;
* KNMI data: Process the downloaded precipitation and potential evaporation and create a hourly raster dataset of the potential evaporation to use as forcing;
* Precipitation NRR Radar: Create NetCDF file and reproject the coordinates to the Wflow_sbm Geul parameterset coordinates.
