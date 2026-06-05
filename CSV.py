import pandas as pd
df = pd.read_csv("product.csv")

df["total_price"] = df["price"] * df["quantity"]
total_sum = df["total_price"].sum()
print(df)
print("Total Sum =", total_sum)

df.to_csv("result.csv", index=False)

