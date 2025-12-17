import pandas as pd
import os

def load_keyrecs_dataset():
    raw_path = "data/keystrokes/summary/per_user_summaries"
    all_files = [f for f in os.listdir(raw_path) if f.endswith(".csv")]
    df_list = []

    for file in all_files:
        full_path = os.path.join(raw_path, file)
        print("Loading:", full_path)
        df = pd.read_csv(full_path)
        df_list.append(df)

    # Merging all CSVs into one dataframe
    final_df = pd.concat(df_list, ignore_index=True)
    print("Dataset shape:", final_df.shape)
    return final_df

if __name__ == "_main_":
    df = load_keyrecs_dataset()
    print(df.head())