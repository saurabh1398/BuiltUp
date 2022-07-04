# Getting Development Indicators: Built-Up area and Percentage Change in Built-Up area at the village level using Landsat-7 Satellite images.

*The following steps need to be followed to generate the Built-Up areas for villages in a state*

1. **Getting district names in a state** 
	First get the names of all the districts in a state and save them as statename_distnames.txt (ex: gujarat_dist_names.txt), inside the District_Names folder in data. A sample text file for gujarat is available. The list of districts in a state according to the 2011 census can be obtained [here](https://www.census2011.co.in/states.php).

2. **Downloading the Landsat 7 images of districts in the state from Google Earth Engine**
	Go to the following url: https://code.earthengine.google.com/
	Upload GEE Assets: [L7_balanced_training_data](/data/GEE_Assets/L7_balanced_training_data.csv) and [district boundary shapefiles](/data/GEE_Assets/district_boundary_shapefiles)
	Paste this [code](/src/landsat7_classification_smote.js) in the editor
	Modify the aoi list to include the district which you wish to download and the year list to include
	the years over which you wish to download the images
	Press Run
	To avoid run and confirm for all districts for all the years: paste this helpler [script](batch_executin_gee.txt) in console on chrome. After pasting both the functions in the console, write runTaskList() in the console to run all the tasks, wait for sometime before the confirmation window pops up, then write ConfirmAll(); in the console to confirm all the tasks.
	After this step, the images of districts in .tif format will be exported to google drive with names: Landsat7_dist_name. 

3. **Cutting villages from the images of districts**
    - Generating district GeoJSON: 
    ```./generate.sh "state_name" "state_shapefile.geojson" "state_dist_names.txt"```
    This will generate .geojson file corresponding to each district in state_dist_names.txt which contains the geometry/boundary of all the villages present in the district. 
    Ex: ```./generate.sh "Gujarat" "GJ.geojson" "gujarat.txt"```
	
    - Cutting the district images: 
    Upload the [script] (/src/cut_vills_from_dist.ipynb) on google colab, upload the .geojson files of the districts generated in previous step that you wish to analyze and select run-all.
	
    After this step, on the google drive, for each district a Folder with name Villages will be created that contains the .tif images of the villages present in the district. Download the folder for each district in /data/IndiaSat.

4. **Applying Landuse Classifier on the village Images**
	```run ./eval.sh "state_dist_names.txt"```
	This step will apply Landuse classfier to images of the villages. The results for each district will be stored in /data/IndiaSat/Results

5. **Computing Built-Up**
	Once, we get the output of the Landuse Classifier, run the following commang: 
	```./final_vill.sh "state_name" "state_dist_names.txt"``` 
	This step will generate a .csv file in /results containing the following columns:
	Village Code, Village Name, District Name, Built-Up 2013, Built-Up 2019, Percentage Change in Built-Up.



Some points to keep in mind
- Verify that the names in the textfile are present and are unique in india_district_boundaries.geojson. For ex: Aurangabad district is present in both Maharashtra and Bihar. In that case, change the name of Aurangabad in Maharashtra to: Aurangabad_maha. After this step you will have to regnerate the shapefiles. (use geopandas in python) 
- The last line in the textfile containing the names of the districts should be \n or blank or the last district will be skipped
