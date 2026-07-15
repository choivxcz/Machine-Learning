import pandas as pd
from sklearn.preprocessing import OneHotEncoder

d = {'City': ['Tampa', 'Orlando', 'Tampa', 'Miami', 'Jacksonville', 'Tampa', 'Orlando', 'Miami', 'Jacksonville', 'Tampa'],
'Size': ['small', 'medium', 'large', 'small', 'medium', 'large', 'small', 'medium', 'large', 'small']}

df = pd.DataFrame(data=d)

print(df['City'].unique())

ohe = OneHotEncoder(sparse_output=False).set_output(transform="pandas")

ohetransform = ohe.fit_transform(df[['City']])

print(ohetransform)

print(df.join(ohetransform).drop(columns=['City']))