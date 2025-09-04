import glob
import pandas as pd


csv_files = glob.glob("data/*.csv")

dfs = []
for file in csv_files:
    df = pd.read_csv(file)
    df= df[df["product"] == "pink morsel"]
    df["price"] = df["price"].replace('[$]', '', regex=True)
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["sales"] = df["price"] * df["quantity"]
    df = df[["sales", "date", "region"]]

dfs.append(df)
final_df = pd.concat(dfs, ignore_index=True)
final_df.to_csv("formatted_sales.csv", index=False)