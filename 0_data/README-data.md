**Step 1** In folder "0_data/" create two folders:
- "0_data/2023-citibike-tripdata"
- "0_data/2025-police-data"

**Step 2** Import data for CitiBike Rides 2023 
- Download "2023-citibike-tripdata.zip" under [CitiBike](https://s3.amazonaws.com/tripdata/index.html )
- Un-zip to .CSV files
- Save CSV files in "0_data/2023-citibike-tripdata"

**Step 3** Import data for NYPD 
- Download "Motor Vehicle Collisions - Crashes" under [NYPD](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/about_data)
- Save CSV file in "0_data/2025-police-data"

**Step 4** Pre-processing of data by running the following scripts
- "2_scripts/0_preprocess-citibike-data.py" 
- "2_scripts/1_preprocess-police-data.py"

Now you have all data to run the code in the notebooks!