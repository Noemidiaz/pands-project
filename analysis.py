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

# Prints the number of rows and columns in the dataset: 150 rows and 5 columns.
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

# Variable 1: Species (object). Each type is equally represented (5 Iris setosa, 50 Iris virginica and 50 Iris versicolor).It is a balanced data set.

# Variable X is species. 
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
# Save the plot to a file (in this case png file)
plt.savefig('species_histogram.png')
# Show the plot
plt.show()



# Variable 2: Sepal length (float).

# Variable X is sepal length. 
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
# Save the plot to a file (in this case png file)
plt.savefig('sepal_length_histogram.png')
# Show the plot
plt.show()

# Variable 3: Sepal width (float)

# Variable X is sepal width. 
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
# Save the plot to a file (in this case png file)
plt.savefig('sepal_width_histogram.png')
# Show the plot
plt.show()

# Variable 4: Petal length (float).

# Variable X is petal length. 
petallen = df['petal_length']
# Show
print(petallen)
#'petal length' is the variable  to plot
petallen = df['petal_length']
# Plotting the histogram
plt.hist(petallen, bins=5, color='rebeccapurple', edgecolor='black')
plt.xlabel('petal length')
plt.ylabel('')
plt.title('Histogram of Iris Petal length')
# Save the plot to a file (in this case png file)
plt.savefig('petal_length_histogram.png')
# Show plot
plt.show()

# Variable 5 : Petal width (float)

# Variable X is petal width. 
petalwd = df['petal_width']
# Show
print(petalwd)
#'petal width' is the variable  to plot
petalwd = df['petal_width']
# Plotting the histogram
plt.hist(petalwd, bins=5, color='rebeccapurple', edgecolor='black')
plt.xlabel('petal width')
plt.ylabel('')
plt.title('Histogram of Iris Petal width')
# Save the plot to a file (in this case png file)
plt.savefig('petal_width_histogram.png')
# Show the plot
plt.show()

# STEP 4. Creating a Scatter plot of each of pair of variables taking into account types of species.

# Scatter Plot 1: Sepal length vs sepal width.

# Extract data for sepal length, sepal width and species.
sepallen = df['sepal_length']
sepalwd = df['sepal_width']
spe = df['species'].unique()

# Define colors and markers for each species in the plot
colors = ['indigo', 'green', 'yellow']  # Different colors for categorize Iris
markers = ['o', '^', 's']          # Different markers for categorize Iris

# Create scatter plot for each species
plt.figure(figsize=(10, 8))
for i, species in enumerate(spe):
    species_data = df[df['species'] == species]
    plt.scatter(species_data['sepal_length'], species_data['sepal_width'], color=colors[i], marker=markers[i], label=species, alpha=0.7)

# Decorative details in the plot
plt.title('Scatter Plot of Sepal Length vs Sepal Width by Species')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
# Save the plot to a file (in this case png file)
plt.savefig('Sepal_Length_Sepal_Width_Scatter_Plot.png')
# Show the plot.
plt.show()

# Scatter Plot 2: Petal length vs Petal width.

# Extract data for petal length , petal width and species.
petallen = df['petal_length']
petalwd = df['petal_width']
spe = df['species'].unique()

# Define colors and markers for each species in the plot.
colors = ['indigo', 'green', 'yellow']  # Different colors for categorize Iris
markers = ['o', '^', 's']          # Different markers for categorize Iris

# Create scatter plot for each species
plt.figure(figsize=(10, 8))
for i, species in enumerate(spe):
    species_data = df[df['species'] == species]
    plt.scatter(species_data['petal_length'], species_data['petal_width'], color=colors[i], marker=markers[i], label=species, alpha=0.7)

# Decorative details in the plot
plt.title('Scatter Plot of Petal Length vs Petal Width by Species')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.legend()
# Save the plot to a file (in this case png file)
plt.savefig('Petal_Length_Petal_Width_Scatter_Plot.png')
# Show the plot.
plt.show()

# End