import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder

df = pd.read_csv("employeesOHEEN.csv")

print(df.head())

df.drop(columns = ["name"], inplace=True)

print(df.head())

print(df["education_level"].unique())

education_levels = [
    "High School",
    "Bachelor's",
    "Master's",
    "PhD"
]

performance_ratings = [
    "Poor",
    "Average",
    "Good",
    "Excellent"
]
enc = OrdinalEncoder(categories=[education_levels, performance_ratings])
df[["education_level", "performance_rating"]] = enc.fit_transform(df[["education_level", "performance_rating"]])

print(df)

ohe = OneHotEncoder(sparse_output=False).set_output(transform="pandas")

ohetransform = ohe.fit_transform(df[["department"]])

print(ohetransform)

print(df.join(ohetransform).drop(columns=['department']))