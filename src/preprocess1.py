'''
Need to drop certain features after EDA because,
- min, median, percentile_25:  always 0
- nan_fraction:  always same value
- zero_fraction:  exact opposite of non_zero_fraction so only keep one
'''

import pandas as pd

def clean_features(df):
    drop_cols = [
        "min",
        "median",
        "nan_fraction",
        "percentile_25",
        "zero_fraction"  
    ]

    df_clean = df.drop(columns=drop_cols, errors="ignore")

    print("Cleaned dataset shape:", df_clean.shape)
    return df_clean


if __name__ == "__main__":
    df = pd.read_csv("data/keystrokes/processed/keystroke_features.csv")
    df_clean = clean_features(df)
    print(df_clean.head())
    df_clean.to_csv("data/keystrokes/processed/keystroke_features_clean.csv", index=False)
    print("Saved cleaned dataset!")

