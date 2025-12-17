import pandas as pd
import numpy as np
import os


def load_dataset(csv_path):
    print(f"Loading dataset from: {csv_path}")
    df = pd.read_csv(csv_path)
    print("Dataset shape:", df.shape)
    return df


def compute_summary_features(df):
    # Timing columns: DU.v.v - total time
    timing_cols = df.columns[3:-1]

    # Summary statistics per row (per typing attempt)
    df["mean_timing"] = df[timing_cols].mean(axis=1)
    df["median_timing"] = df[timing_cols].median(axis=1)
    df["std_timing"] = df[timing_cols].std(axis=1)
    df["max_timing"] = df[timing_cols].max(axis=1)

    return df


def export_per_user_csvs(df, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    output_cols = [
        "participant",
        "session",
        "repetition",
        "mean_timing",
        "median_timing",
        "std_timing",
        "max_timing",
        "total time"
    ]

    summary_df = df[output_cols]

    for participant_id, user_df in summary_df.groupby("participant"):
        out_path = os.path.join(output_dir, f"{participant_id}_summary.csv")
        user_df.to_csv(out_path, index=False)
        print(f"Saved: {out_path}")


if __name__ == "__main__":
    INPUT_CSV = "data/keystrokes/raw/fixed-text.csv"
    OUTPUT_DIR = "data/keystrokes/summary/per_user_summaries"

    # 1. Load
    df = load_dataset(INPUT_CSV)
    # 2. Compute summaries
    df = compute_summary_features(df)
    # 3. Export per participant
    export_per_user_csvs(df, OUTPUT_DIR)

    print("All processing complete.")
