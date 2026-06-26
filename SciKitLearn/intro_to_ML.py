#this file contains the tutorial of Machine Learning from freecodecamp full course

import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas  as pd
import numpy as np

my_df = pd.read_csv("medical.csv")
print(my_df)
print(my_df.info())
"""fig = px.histogram(my_df, x = "smoker", color = "sex", title = "Smoker Distribution")
fig.show()"""

"""fig  = px.scatter(my_df, x = "age", y = "charges", color = "smoker", opacity = 0.8, title = "Age vs Charges by Smoker Status")
fig.show() """

fig = px.violin(my_df, x = "smoker", y = "charges", color = "sex", box = True, points = "all", title = "Charges Distribution by Smoker Status and Sex")
fig.show()