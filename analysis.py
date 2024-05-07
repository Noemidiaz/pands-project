# analysis.py
# This is my code used for the analysis of Fisher's Iris data set
# Author: Noemi Diaz


# Imports and libraries

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# STEP 1: Load and save dataset.

# Loading Iris data from seaborn
df = pd.read_csv ("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Download and save the Iris dataset to a file in the repository
df.to_csv("iris.csv", index=False)


# STEP 2.Examining data set.

# Have a look the data
print(df) 

# Describe the data set
print(df.describe())

# prints the number of rows and columns in the dataset
print(df.shape)

# Look at the first row
print (df.iloc [0])

# Analysis of the species
print (df ["species"])

# Count the number of Iris of each species type
print (df["species"].value_counts())


# STEP 3. Types of variables

# Inspect types of variables
print(df.dtypes)


# STEP 4. One variable Plot

# cherry pie Iris species type
# STEP 4. scatter plot of each of pair of variables
