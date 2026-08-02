import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

df = pd.read_csv("coffee_orders.csv")

print(df.head())

df.drop(columns = ["customer_name"], inplace=True)

cup_sizes = ["Small", "Medium", "Large"]
membership_tiers = ["Bronze", "Silver", "Gold", "Platinum"]
enc = OrdinalEncoder(categories=[cup_sizes, membership_tiers])

df[["cup_size", "membership_tier"]] = enc.fit_transform(df[["cup_size", "membership_tier"]])

print(df)