import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report

df = pd.read_csv("500hits.csv", encoding="latin-1")
print(df.head())

df = df.drop(columns = ["PLAYER", "CS"])

print(df.head())

X = df.iloc[:, 0:13]
y = df["HOF"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=11, test_size=0.2)

scaler = MinMaxScaler(feature_range=(0, 1))
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
knn = KNeighborsClassifier(n_neighbors=8)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

print(y_pred)

cm = confusion_matrix(y_test, y_pred)
cr = classification_report(y_test, y_pred)
print(cr)