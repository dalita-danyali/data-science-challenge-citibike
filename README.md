# data-science-challenge-citibike
Solution for AXA data science challenge. We explore risks and design a potential insurance cooperation by analysing data from CitiBike and New York Police Department (NYPD) in 2023.

### About
This project explores CitiBike trips and NYPD crash data (2023). The goal is to identify risk patterns, quantify exposure, and propose how CitiBike and AXA could collaborate to improve rider safety and design insurance products.

### Data
The code uses the following publicly available data.
- **CitiBike Rides 2023**: "2023-citibike-tripdata.zip" under [CitiBike](https://s3.amazonaws.com/tripdata/index.html )
- **NYPD Crash Data 2023**: "Motor Vehicle Collisions - Crashes" under [NYPD](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/about_data)

The data includes infromation on the individual rides (e.g., timestamps, location, membership) and accidents in New York (e.g., timestamps, location, injuries, vehicles).

Details on data pre-processing in `0_data/README-data.md`

Latest download on 13.09.2025

### Analysis
Analysis is performed in a Jupyter notebook `1_notebooks/1_analysis.ipynb`, while initial thoughts are tested in `1_notebooks/0_playground.ipynb`. 

## Setup & Installation
1. Clone this repo: `git clone https://github.com/dalita-danyali/data-science-challenge-citibike.git`
2. Install requirements: `pip install -r requirements.txt`
3. Perform data pre-processing as described in `0_data/README-data.md`
3. Open and run `1_notebooks/1_analysis.ipynb` in Jupyter or VSCode