import pandas as pd

df = pd.read_csv("customer_data.csv")

print("Before Cleaning:")
print(df)

df = df.drop_duplicates()
df = df.dropna()

print("\nAfter Cleaning:")
print(df)
