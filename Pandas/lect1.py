import pandas as pd

# Path of the file to read
iowa_file_path = 'train.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(iowa_file_path)
print(df.head())

avg_lot_price = df['LotArea'].mean()
newest_home_age = df['YearBuilt'].max()
print("New Home Age:", newest_home_age)
print("Average Lot Price:", avg_lot_price)