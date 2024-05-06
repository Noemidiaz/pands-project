# analysis.py
# 
# Author: Noemi Diaz


# Imports and libraries

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# Load the data 

df = pd.read_csv ("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")


# Examining data set
# Have a look the data
print(df) 

# Look at the first row
print (df.iloc [0])

# Analysis of the species
print (df ["species"])
