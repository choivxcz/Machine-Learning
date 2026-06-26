import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt

def basics():
    print("Basics of Scikit-learn")
    data = pd.read_csv("student_performance.csv")
    print(data)
    my_df = pd.DataFrame(data)
    print(my_df)
    X = my_df.drop("final_grade", axis=1)
    print(X)
    y = my_df["final_grade"]
    print(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    print(X_train.shape)
    print(X_test.shape)
    print(y_train.shape)
    print(y_test.shape)
    
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    y_pred = lr.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    intercept = lr.intercept_
    
    print("R2 Score:", r2)
    print("Mean Squared Error:", mse)
    print("Mean Absolute Error:", mae)
    print("Intercept:", intercept)
    
    plt.scatter(y_test, y_pred)
    plt.plot([y.min(), y.max()], [y.min(), y.max()], color="Green")
    plt.xlabel("True Values")
    plt.ylabel("Predicted Values")
    plt.title("ALinear Regression")
    plt.show()
    print("end of basics")

print(basics())