'''
What this file does:
    1. Load ALL user CSV files
    2. Add a “user_id” column
    3. Merge them into 1 big dataset
    4. Convert 808 raw columns into nice features
    5. Save this as a new usable ML dataset
'''


import pandas as pd
import numpy as np
import os

def fullRaw():
    raw_path = "data/keystrokes/raw"
    all_files = [f for f in os.listdir(raw_path) if f.endswith(".csv")]

    df_list = []
    for file in all_files:
        #data/keystrokes/raw/user_(user_id).csv
        full_path = os.path.join(raw_path, file) 
        df = pd.read_csv(full_path)

        user_id = int(file.split("_")[1].split(".")[0])  
        df["user_id"] = user_id

        df_list.append(df)

    full_df = pd.concat(df_list, ignore_index=True)
    return full_df

def featureDataset(raw_df):
    # Omit the user_id column to get numeric data only
    labels = raw_df["user_id"]
    raw_df = raw_df.drop(columns=["user_id"])

    numeric_df = raw_df.apply(pd.to_numeric, errors='coerce')
    feature_df = pd.DataFrame({
        "mean": numeric_df.mean(axis=1),
        "std": numeric_df.std(axis=1),
        "max": numeric_df.max(axis=1),
        "min": numeric_df.min(axis=1),
        "median": numeric_df.median(axis=1),
        "non_zero_fraction": (numeric_df != 0).sum(axis=1) / numeric_df.shape[1],
        "zero_fraction": (numeric_df == 0).sum(axis=1) / numeric_df.shape[1],
        "nan_fraction": numeric_df.isna().sum(axis=1) / numeric_df.shape[1],
        "percentile_25": numeric_df.quantile(0.25, axis=1),
        "percentile_75": numeric_df.quantile(0.75, axis=1)
    })

    feature_df["user_id"] = labels

    return feature_df

if __name__ == "__main__":
    raw_df = fullRaw()
    print("Raw dataset shape:", raw_df.shape)

    processed_df = featureDataset(raw_df)
    print("Processed dataset shape:", processed_df.shape)

    processed_df.to_csv("data/keystrokes/processed/keystroke_features.csv", index=False)
    print("Saved processed dataset to data/processed!")



    
