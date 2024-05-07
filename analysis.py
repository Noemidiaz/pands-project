# analysis.py
# This is my analysis of Fisher's Iris data set
# Author: Noemi Diaz


# Imports and libraries

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# Loading Iris data from seaborn

df = pd.read_csv ("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")


# Examining data set
# Have a look the data
print(df) 

# prints the no of rows and columns in the dataset
print(df.shape)

# Look at the first row
print (df.iloc [0])

# Analysis of the species
print (df ["species"])

# Count Iris of each species
print (df["species"].value_counts())