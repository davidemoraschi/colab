# Importing the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
dataset = pd.read_csv('titanic.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print(X)
print(y)

# Identify the categorical data


# Implement an instance of the ColumnTransformer class


# Apply the fit_transform method on the instance of ColumnTransformer


# Convert the output into a NumPy array


# Use LabelEncoder to encode binary categorical data


# Print the updated matrix of features and the dependent variable vector

