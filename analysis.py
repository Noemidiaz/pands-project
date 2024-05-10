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

# Have a look the data.
print(df) 

# Describe the data set.
print(df.describe())

# prints the number of rows and columns in the dataset: 150 rows and 5 columns.
print(df.shape)

# Look at the first row.
print (df.iloc [0])

# Analysis of the species
print (df ["species"])

# Count the number of Iris of each species type
print (df["species"].value_counts())


# STEP 3. Inspect types of variables

# Types of variables
print(df.dtypes)


# STEP 4.  Creating a Histogram for each variable.

# Variable 1: Species (object). Each type is equally represented.

# Variable x is species. 
spe = df['species']
# Show
print(spe)
#'species' is the variable  to plot
spe = df['species']
# Plotting the histogram
plt.hist(spe, bins=5, color='Thistle', edgecolor='black')
plt.xlabel('species')
plt.ylabel('')
plt.title('Histogram of Iris species')
plt.show()

# Creating a pie chart to visualize types of Iris species

y = np.array([50, 50, 50])
mylabels = ["Setosa", "Versicolor", "Virginica"]

plt.pie(y, labels = mylabels)
plt.title("Types of Iris species")
plt.show() 

# Variable 2: Sepal length (float).

# Variable x is sepal length. 
sepallen = df['sepal_length']
# Show
print(sepallen)
#'sepal length' is the variable  to plot
sepallen = df['sepal_length']
# Plotting the histogram
plt.hist(sepallen, bins=5, color='rebeccapurple', edgecolor='black')
plt.xlabel('sepal length')
plt.ylabel('')
plt.title('Histogram of Iris Sepal Length')
plt.show()

# Variable 3: sepal width (float)

# Variable x is sepal width. 
sepalwd = df['sepal_width']
# Show
print(sepalwd)
#'sepal width' is the variable  to plot
sepalwd = df['sepal_width']
# Plotting the histogram
plt.hist(sepalwd, bins=5, color='rebeccapurple', edgecolor='black')
plt.xlabel('sepal width')
plt.ylabel('')
plt.title('Histogram of Iris Sepal width')
plt.show()

# Variable 4: Petal length (float).

# Variable x is petal length. 
petallen = df['petal_length']
# Show
print(petallen)
#'sepal width' is the variable  to plot
petallen = df['petal_length']
# Plotting the histogram
plt.hist(petallen, bins=5, color='rebeccapurple', edgecolor='black')
plt.xlabel('petal length')
plt.ylabel('')
plt.title('Histogram of Iris Petal length')
plt.show()

# Variable 5 : Petal width (float)

# Variable x is petal width. 
petalwd = df['petal_width']
# Show
print(petalwd)
#'sepal width' is the variable  to plot
petalwd = df['petal_width']
# Plotting the histogram
plt.hist(petalwd, bins=5, color='rebeccapurple', edgecolor='black')
plt.xlabel('petal width')
plt.ylabel('')
plt.title('Histogram of Iris Petal width')
plt.show()

# STEP 4. scatter plot of each of pair of variables
