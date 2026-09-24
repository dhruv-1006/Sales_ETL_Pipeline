import pandas as pd
import sqlite3

# EXTRACT
df = pd.read_csv("sales.csv")
print(df)
print(df.info())

# TRANSFORM
df = df.drop_duplicates()
df["customer"] = df["customer"].str.strip().str.title()
df["product"] = df["product"].str.strip().str.title()
df["quantity"] = df["quantity"].fillna(1).astype(int)
df["order_date"] = pd.to_datetime(df["order_date"])
df["total"] = df["quantity"] * df["price"]

print(df)

# LOAD
import sqlite3
conn = sqlite3.connect("sales.db")
df.to_sql("sales", conn, if_exists="replace", index=False)
conn.close()
print("Loaded into sales.db")