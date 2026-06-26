import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from numpy.random import randn

def series():
    print("Series in Pandas")
    my_series = [1, 2, 3, 4, 5]
    #turns list into a series
    my_var = pd.Series(my_series)

    print(my_var)

    my_index = ['a', 'b', 'c', 'd', 'e']
    #turns list into a series with index
    my_indexed_variable = pd.Series(my_series, index= my_index)

    print(my_indexed_variable)

    cars = {'Tesla': 2020, 'BMW': 2019, 'Audi': 2021}

    print(pd.Series(cars))
    print("End of Series in Pandas")

#print(series())

def challenge1():
    price = [5, 10, 15]
    food_index = ["sinigang", "adobo", "tinola"]
    
    food_price = pd.Series(price, index=food_index)
    print(food_price)
    
    scores = pd.Series([88, 92, 75, 60, 95], 
    index=['Ana', 'Ben', 'Carlo', 'Diana', 'Earl'])
    print(scores["Carlo"])
    print(scores[1:4])
    
    laguna = {
    'Santa Cruz': 120000,
    'Calamba': 450000,
    'Los Baños': 85000,
    'Pagsanjan': 35000,
    'Sta. Rosa': 380000
    }
    print(pd.Series(laguna))
    for i in laguna:
        if laguna[i] > 100000:
            print(i)
            
    grades = pd.Series([88, 92, 75, 60, 95, 78, 83])
    print(grades.mean())
    print(grades.max())
    print(grades.min())
    print((grades >= 90).sum())

#print(challenge1())

def Data_Frame():
    print("DataFrame in Pandas")
    data = randn(10, 7)
    rows = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    columns = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    my_dataframe = pd.DataFrame(data, rows, columns)
    print(my_dataframe)
    my_csvdata = pd.read_csv("students.csv")
    print(my_csvdata)
    print(my_csvdata.loc[0])
    print(my_csvdata["grade"].describe())
    print(my_csvdata.head(9))
    print(my_csvdata.tail(3))
    print(my_csvdata.region)
    print("End of DataFrame in Pandas")

#print(Data_Frame())

def data_count():
    print("Data Count in Pandas")
    my_csvdata = pd.read_csv("students.csv")
    print(my_csvdata)
    print(my_csvdata["name"].value_counts())
    print(my_csvdata["region"].value_counts())
    print(my_csvdata["region"].value_counts(normalize = True))
    print(my_csvdata["region"].value_counts()['Laguna'])
    print("End of Data Count in Pandas")

#print(data_count())

def challenge2():
    print("Challenge 2")
    my_data = pd.read_csv("students2.csv")
    print(my_data)
    print(my_data.head(5))
    print(my_data["grade"].describe())
    print(my_data["region"] == "Laguna")
    print(my_data["name"][my_data["grade"] >= 75])
    print(my_data["name"][my_data["region"] == "Laguna"][my_data["grade"] >= 75])
    print(my_data["region"].value_counts())
    print(my_data["region"].value_counts(normalize=True))
    print(my_data["subject"].value_counts())
    print(my_data["grade"].mean())
    print(my_data["name"][my_data["grade"] < 75])
    print(my_data["attendance"].max())
    my_series = pd.Series(my_data["name"][my_data["grade"] >= 75][my_data["attendance"] >= 80])
    print(my_series)
    print(my_series.count())
#print(challenge2())

def insert_column():
    print("Insert Column in Pandas")
    my_data = pd.read_csv("students2.csv")
    print(my_data)
    my_data["passed"] = my_data["grade"] >= 75
    print(my_data)
    print(my_data.assign(Graduating=[True]*len(my_data)))
    print("End of Insert Column in Pandas")
    
#print(insert_column())

def delete_row_column():
    print("Delete Row/Column in Pandas") 
    my_data = pd.read_csv("students2.csv")
    print(my_data)
    print(my_data.drop("name", axis=1))
    print(my_data.drop(my_data.index[0:5], axis=0))
    print("End of Delete Row/Column in Pandas")

#print(delete_row_column())

def challenge3():
    print("Challenge 3")
    my_data = pd.read_csv("school.csv")
    print(my_data)
    print("Challenge 3:1")
    print(my_data.tail(4))
    print(my_data["age"].describe())
    print(my_data.loc[2])
    print("Challenge 3:2")
    print(my_data[my_data["region"] == "Cavite"])
    print(my_data["name"][my_data["grade"] < 75][my_data["tuition_paid"] == "False"])
    print(my_data["age"].value_counts()[18])
    print("Challenge 3:3") 
    print(my_data["subject"].value_counts(normalize=True))
    print(my_data["region"].value_counts()["Batangas"])
    print("Challenge 3:4")
    print(my_data.assign(Status=np.select([my_data["grade"] >= 90, my_data["grade"] >= 75], ["Excellent", "Passed"], default="Failed")))
    print("Challenge 3:5")
    print(my_data.drop(["tuition_paid", "age"], axis=1))
    print(my_data.drop(my_data.index[7:10], axis=0))
    
#print(challenge3())

def grab_row_pointSubset():
    print("Grab Row/Point/Subsets in Pandas")
    my_data = pd.read_csv("students2.csv")
    print(my_data)
    print(my_data.loc[0])
    print(my_data.iloc[0])
    print(my_data.loc[0:5])
    print(my_data.iloc[0:5])
    print(my_data.loc[0:5, "name"])
    print(my_data.iloc[0:5, 0])
    print("End of Grab Row/Point/Subsets in Pandas")

#print(grab_row_pointSubset())

def conditional_selection():
    print("Conditional Selection in Pandas")
    my_data = pd.read_csv("students2.csv")
    print(my_data)
    print(my_data["grade"] >=75)
    print(my_data == "Juan")
    print(my_data == "Laguna")
    print("End of Conditional Selection in Pandas")
    
#print(conditional_selection())

def mixed_conditional_selection():
    print("Mixed Conditional Selection in Pandas")
    my_data = pd.read_csv("students2.csv")
    print(my_data)
    print(my_data[(my_data["region"] == "Laguna") & (my_data["grade"] >= 50)]["name"])
    print(len(my_data[(my_data["region"] == "Laguna") & (my_data["grade"] >= 75)])) 
    print("End of Mixed Conditional Selection in Pandas")

#print(mixed_conditional_selection())

def challenge4():
    print("Challenge 4")
    my_data = pd.read_csv("barangay.csv")
    print(my_data)
    print("Challenge 4:1")
    print(my_data.loc[3])
    print(my_data.iloc[3])
    print("")
    print(my_data.loc[2:5])
    print(my_data.iloc[2:6])
    print("loc includes the last index while iloc does not include the last index")
    print(my_data.loc[0:4, ["name", "barangay"]])
    print("Challenge 4:2")
    print(my_data["employed"] == True)
    print(my_data[my_data["barangay"] == "Poblacion"])
    print(my_data[my_data["monthly_income"] >= 15000]["name"])
    print("")
    print("Challenge 4:3")
    print(my_data[(my_data["employed"] == True) & (my_data["barangay"] == "Bagumbayan")])
    print(my_data[(my_data["employed"] == False) | (my_data["monthly_income"] < 8000)])
    print(my_data[(my_data["age"] > 30) & (my_data["years_residing"] > 8)])
    print("")
    print("Challenge 4:4")
    print(my_data.assign(income_class = np.select([my_data["monthly_income"] >= 25000, my_data["monthly_income"] >= 10000], 
                                                  ["High Income", "Middle Income"], default="Low Income")))
    print(my_data.drop("years_residing", axis=1))
    print("")
    print("Challenge 4:5")
    print(my_data["monthly_income"].groupby(my_data["barangay"]).mean())
    print(my_data["barangay"].value_counts())
    print(my_data["employed"].mean())
    print("End of Challenge 4")
    
#print(challenge4())

def incomplete():
    print("Incomplete")
    my_data = pd.read_csv("dirty_data.csv")
    print(my_data)
    print(my_data.isnull())
    #drop all rows with missing values
    print(my_data.dropna())
    #drop all columns with missing values if rows use 0 or default
    print(my_data.dropna(axis=1))
    #fill missing values with 0 or default
    print(my_data.fillna(0))
    #drop rows with at least 5 non-missing values
    print(my_data.dropna(thresh=5, axis=0))
    print("End of Incomplete")

#print(incomplete())

def my_groupby():
    print("Groupby in Pandas")
    stuff = {
    'Corporation': ['Apple', 'Google', 'Meta', 'Apple', 'Google', 'Meta'],
    'Employees': ['John', 'April', 'Wes', 'Beth', 'Justin', 'Steph'],
    'Salary': [200, 220, 190, 130, 120, 150]
    }
    my_data = pd.DataFrame(stuff)
    
    print(my_data)
    print(my_data.groupby("Corporation")["Salary"].sum())
    print(my_data.groupby("Corporation")["Salary"].mean())
    print(my_data.groupby("Corporation")["Salary"].max())
    print(my_data.groupby("Corporation")["Salary"].min())
    print(my_data.groupby("Corporation")["Salary"].count())
    print(my_data.groupby("Corporation")["Salary"].std())
    print(my_data.groupby("Corporation")["Salary"].var())
    print(my_data.groupby("Corporation")["Salary"].describe())
    print("End of Groupby in Pandas")

#print(my_groupby())

def unique_values():
    print("Unique Values in Pandas")
    my_data = pd.read_csv("students2.csv")
    print(my_data)
    print(pd.DataFrame(my_data["attendance"].unique()))
    print(pd.DataFrame(my_data["region"].unique()).head(1))

    print("End of Unique Values in Pandas")

#print(unique_values())

def function_application():
    print("Function Application in Pandas")
    my_data = pd.read_csv("students2.csv")
    print(my_data)
    def grade_category(grade):
        if grade >= 90:
            return "Excellent"
        elif grade >= 75:
            return "Passed"
        else:
            return "Failed"
    print(pd.DataFrame(my_data["attendance"].apply(grade_category)))
    def attendance_checker(attendance):
            if attendance > 70:
                return "Passed"
            else:
                return "Failed"
    print(pd.DataFrame(my_data["attendance"].apply(attendance_checker)))
    print(pd.DataFrame(((my_data["grade"] >= 85) & (my_data["attendance"] >= 70)).apply(lambda x: "Passed" if x else "Failed"), columns=["Remarks"]))
    print("End of Function Application in Pandas")
    
#print(function_application())

def challenge5():
    print("Challenge 5")
    my_data = pd.read_csv("employees.csv")
    print(my_data)
    print("Challenge 5:1")
    print(my_data.isnull().sum())
    my_data["salary"] = my_data["salary"].fillna(my_data.groupby("department")["salary"].transform("mean"))
    print(pd.DataFrame(my_data))
    print(pd.DataFrame(my_data["department"].dropna()))
    print("Challenge 5:2")
    
    def performance_rank(performance_score):
        if performance_score >= 90:
            return "S"
        elif performance_score >= 75:
            return "A"
        elif performance_score >= 60:
            return "B"
        else:
            return "C"
    
    my_data["performance_rank"] = my_data["performance"].apply(performance_rank)
    print(my_data)
    print("Challenge 5:3")
    print(my_data.groupby("department")["salary"].mean())
    print(my_data.groupby("department")["performance"].max())
    print(my_data.groupby("department")["name"].count())
    print("Challenge 5:4")
    my_data["bonus_eligible"] = my_data["performance"].apply(lambda x: True if x >= 75 else False)
    print(my_data[my_data["bonus_eligible"] == True])
    percent_bonus_eligible = (my_data["bonus_eligible"].sum() / len(my_data)) * 100
    print(f"Percentage of employees eligible for bonus: {percent_bonus_eligible:.2f}%")
    print("Challenge 5:5")
    print(my_data[["name", "department", "salary", "performance_rank", "bonus_eligible"]][my_data["attendance"] >= 70].sort_values(by="salary", ascending=False))
    print("End of Challenge 5")

#print(challenge5())

def histogram():
    print("Histogram in Pandas")
    my_df = pd.DataFrame(randn(25, 4), columns=['A', 'B', 'C', 'D'])
    print(my_df)
    my_df[["A", "B"]].abs().plot(kind = 'line', x = 'A', y = 'B', alpha = 0.5, legend = True, title = "Area Plot", style = 'ggplot', stacked = True, grid = True, figsize = (30, 20))
    plt.show()
    print("End of Histogram in Pandas")

print(histogram())
    
