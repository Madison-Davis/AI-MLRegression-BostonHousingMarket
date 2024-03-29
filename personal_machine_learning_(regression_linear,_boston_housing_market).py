# -*- coding: utf-8 -*-
"""Personal: Machine Learning (Regression: Linear, Boston Housing Market).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11t0Av6CZ__qC-zvNGV6YlvdDvmaeWbhP
"""

# Regression of Boston Housing Market
# Highest Accuracy: 76%, Linear Regression

# Installations
import csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Data Manipulation
# Data Column Input:
  # 0: CRIM: per capita crime rate by town
  # 1: ZN: proportion of residential land zoned for lots over 25,000 sq.ft.
  # 2: INDUS: proportion of non-retail business acres per town
  # 3: CHAS: Charles River dummy variable (1 if tract bounds river; 0 otherwise)
  # 4: NOX: nitric oxides concentration (parts per 10 million) [parts/10M]
  # 5: RM: average number of rooms per dwelling
  # 6: AGE: proportion of owner-occupied units built prior to 1940
  # 7: DIS: weighted distances to five Boston employment centres
  # 8: RAD: index of accessibility to radial highways
  # 9: TAX: full-value property-tax rate per $10,000 [$/10k]
  # 10: PTRATIO: pupil-teacher ratio by town
  # 11: B: The result of the equation B=1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
  # 12: LSTAT: % lower status of the population

# Spectral Class Output:
  # 13: MEDV: Median value of owner-occupied homes in $1000's [k$]

# Training File
dataFile = open("//content//drive//MyDrive//Coding//Personal Projects//3: Machine Learning//Resources//BostonHousingMarket.csv")
data = csv.reader(dataFile)
x = []
y = []

header = True
for row in data:
  if header:
    header = False
    continue
  else:
    y.append(float(row[13]))
    i = 0
    input_values = []
    while i < 13:
      input_values.append(float(row[i]))
      i = i + 1
    x.append(input_values)
  
standardizer = StandardScaler()
x = standardizer.fit_transform(x)

# Test Model: Linear Regression
x_train, x_test, y_train, y_test = train_test_split(x, y , test_size = 0.20, random_state = 1)
model = LinearRegression()
model.fit(x_train, y_train)
accuracy = model.score(x_test, y_test)
accuracy = accuracy * 100
print("Accuracy:", accuracy, "%")