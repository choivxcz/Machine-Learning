import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

d = {'City': ['Tampa', 'Orlando', 'Tampa', 'Miami', 'Jacksonville', 'Tampa', 'Orlando', 'Miami', 'Jacksonville', 'Tampa'],
'Size': ['small', 'medium', 'large', 'small', 'medium', 'large', 'small', 'medium', 'large', 'small']}

df = pd.DataFrame(data=d)

print(df['Size'].unique())

sizes = ['small', 'medium', 'large']
enc = OrdinalEncoder(categories=[sizes])
df['Size'] = enc.fit_transform(df[['Size']])

print(df)



