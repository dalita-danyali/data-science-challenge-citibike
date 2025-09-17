import pandas as pd
import os

if __name__ == "__main__":
    # Load police data set about accidents
    path_p = "../0_data/2025-police-data/Motor_Vehicle_Collisions_-_Crashes_20250908.csv"
    df_p = pd.read_csv(path_p, dtype={"VEHICLE TYPE CODE 1": "string","VEHICLE TYPE CODE 2": "string","VEHICLE TYPE CODE 3": "string","VEHICLE TYPE CODE 4": "string","VEHICLE TYPE CODE 5": "string"})

    # Convert to numeric and set errors to NA, e.g., rows with multiple spaces
    df_p["ZIP CODE"] = pd.to_numeric(df_p["ZIP CODE"], errors="coerce")

    # Set dtypes
    df_p["ZIP CODE"] = df_p["ZIP CODE"].astype("Int64")
    df_p["CRASH DATE"] = pd.to_datetime(df_p["CRASH DATE"])

    # Filter for 2023
    df_p = df_p[df_p["CRASH DATE"].dt.year == 2023]

    # Preparation to filter for accidents that involve cyclists
    cols = [
        "VEHICLE TYPE CODE 1",
        "VEHICLE TYPE CODE 2",
        "VEHICLE TYPE CODE 3",
        "VEHICLE TYPE CODE 4",
        "VEHICLE TYPE CODE 5"
    ]

    df_p["VEHICLE TYPES CONCAT"] = df_p[cols].fillna("").agg(" ".join, axis=1)

    # In column "VEHICLE TYPES CONCAT5" there are many different values that could refer to a bike. Using ChatGPT this is a filtered list of relevant values that could refer to a bike.
    bike_values = [
        # generic bikes
        "Bike", "PEDAL BIKE", "dirt bike",

        # e-bike variants
        "E-Bike", "e-bike", "EBIKE", "Ebike",

        # minibikes, unicycles etc.
        "Minibike", "Minicycle", "minicycle", "Minicycle", "Minibike",

        # pedicabs
        "Pedicab", "PEDICAB",
    ]

    # build regex pattern from list
    pattern = "|".join(bike_values)

    # three boolean conditions
    cond_killed  = df_p["NUMBER OF CYCLIST KILLED"] >= 1
    cond_injured = df_p["NUMBER OF CYCLIST INJURED"] >= 1
    cond_bike    = df_p["VEHICLE TYPES CONCAT"].str.contains(pattern, case=False)

    # combine with OR
    mask = cond_killed | cond_injured | cond_bike

    # For later use: include bool if bike involved or not
    df_p["BICYCLE INVOLVED"] = mask

    # get month
    df_p["month"] = df_p["CRASH DATE"].dt.month

    # get time by looking at part before :
    df_p["hour"] = df_p["CRASH TIME"].str.split(":").str[0]
    df_p["hour"] = df_p["hour"].astype("Int64")

    # Save final CSV to disk, such that it can be loaded directly
    df_p.to_csv("../0_data/_preprocessed-data/police_2023.csv", index=False)

    print(f"✅ Saved preprocessed data to ../0_data/_preprocessed-data/police_2023.csv")