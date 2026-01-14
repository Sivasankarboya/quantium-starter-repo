import pandas as pd
import glob

csv_files = glob.glob("data/*.csv")

df_list = []
for file in csv_files:
    df = pd.read_csv(file)
    df_list.append(df)

combined_df = pd.concat(df_list, ignore_index=True)

pink_df = combined_df[combined_df["product"] == "Pink Morsel"]

pink_df["sales"] = pink_df["quantity"] * pink_df["price"]

final_df = pink_df[["sales", "date", "region"]]

final_df.to_csv("output.csv", index=False)

print("Data processing completed successfully")
