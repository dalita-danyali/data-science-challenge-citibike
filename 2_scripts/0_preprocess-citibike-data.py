import pandas as pd
import os

if __name__ == "__main__":
    # Path to folder with CSVs
    path_c = "../0_data/2023-citibike-tripdata/"

    # File names of all citibike CSVs for 2023
    files = [
        "202312-citibike-tripdata_3.csv",
        "202301-citibike-tripdata_1.csv",
        "202301-citibike-tripdata_2.csv",
        "202302-citibike-tripdata_1.csv",
        "202302-citibike-tripdata_2.csv",
        "202303-citibike-tripdata_1.csv",
        "202303-citibike-tripdata_2.csv",
        "202303-citibike-tripdata_3.csv",
        "202304-citibike-tripdata_1.csv",
        "202304-citibike-tripdata_2.csv",
        "202304-citibike-tripdata_3.csv",
        "202305-citibike-tripdata_1.csv",
        "202305-citibike-tripdata_2.csv",
        "202305-citibike-tripdata_3.csv",
        "202305-citibike-tripdata_4.csv",
        "202306-citibike-tripdata_1.csv",
        "202306-citibike-tripdata_2.csv",
        "202306-citibike-tripdata_3.csv",
        "202306-citibike-tripdata_4.csv",
        "202307-citibike-tripdata_1.csv",
        "202307-citibike-tripdata_2.csv",
        "202307-citibike-tripdata_3.csv",
        "202307-citibike-tripdata_4.csv",
        "202308-citibike-tripdata_1.csv",
        "202308-citibike-tripdata_2.csv",
        "202308-citibike-tripdata_3.csv",
        "202308-citibike-tripdata_4.csv",
        "202309-citibike-tripdata_1.csv",
        "202309-citibike-tripdata_2.csv",
        "202309-citibike-tripdata_3.csv",
        "202309-citibike-tripdata_4.csv",
        "202310-citibike-tripdata_1.csv",
        "202310-citibike-tripdata_2.csv",
        "202310-citibike-tripdata_3.csv",
        "202310-citibike-tripdata_4.csv",
        "202311-citibike-tripdata_1.csv",
        "202311-citibike-tripdata_2.csv",
        "202311-citibike-tripdata_3.csv",
        "202312-citibike-tripdata_1.csv",
        "202312-citibike-tripdata_2.csv"
    ]

    # Read in all CSVs and rows, but only use a subset of columns. Concatenate them into one dataframe.
    for i in range(len(files)):
        path_temp = path_c + files[i]
        df_temp = pd.read_csv(path_temp,usecols=["rideable_type", "started_at", "ended_at", "start_lat", "start_lng", "end_lat", "end_lng", "member_casual"], parse_dates=["started_at", "ended_at"])
        if i == 0:
            df_c = df_temp
        else:
            df_c = pd.concat([df_c, df_temp], ignore_index=True)

    # Check for 0 duplicates
    df_c.duplicated().sum()

    # Add columns for later averaging
    df_c["month"] = df_c["ended_at"].dt.month
    df_c["hour"] = df_c["ended_at"].dt.hour


    # if not existing create folder for preprocessed data
    if not os.path.exists("../0_data/_preprocessed-data/"):
        os.makedirs("../0_data/_preprocessed-data/")

    # Save final CSV to disk, such that it can be loaded directly
    df_c.to_csv("../0_data/_preprocessed-data/citibike_2023.csv", index=False)

    print(f"✅ Saved preprocessed data to ../0_data/_preprocessed-data/citibike_2023.csv")