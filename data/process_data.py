import pandas as pd

# Load all CSV files
df0 = pd.read_csv("data/daily_sales_data_0.csv")
df1 = pd.read_csv("data/daily_sales_data_1.csv")
df2 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine all data
df = pd.concat([df0, df1, df2], ignore_index=True)

# Convert date to datetime
df["date"] = pd.to_datetime(df["date"])

# Convert price from "$3.00" → 3.00
df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)

# Calculate sales
df["sales"] = df["price"] * df["quantity"]

# Filter only Pink Morsel (important for business question)
df = df[df["product"].str.lower() == "pink morsel"]

# Group by date and sum sales
processed_df = df.groupby("date", as_index=False)["sales"].sum()

# Save processed file
processed_df.to_csv("data/processed_sales_data.csv", index=False)

print("✅ processed_sales_data.csv created successfully")
