from sklearn.impute import SimpleImputer
import pandas as pd

df = pd.read_csv("sarisari_sales.csv")

print(df.head())
print(df.isnull().sum())

imputer_price = SimpleImputer(strategy="mean")
df[["price"]] = imputer_price.fit_transform(df[["price"]])

impute_quantity = SimpleImputer(strategy="mean")
df[["quantity_sold"]] = impute_quantity.fit_transform(df[["quantity_sold"]])

impute_age = SimpleImputer(strategy="mean")
df[["customer_age"]] = impute_age.fit_transform(df[["customer_age"]])

impute_payment = SimpleImputer(strategy="constant", fill_value="Unknown")
df[["payment_method"]] = impute_payment.fit_transform(df[["payment_method"]])

print(df)
print(df.isnull().sum())
