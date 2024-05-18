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


# STEP 2. Inspect types of variables.

# Types of variables
print(df.dtypes)


# STEP 3.Examining data set.

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

# Calculate the measure mean of numerical variables (float)
print(df[["sepal_length","sepal_width", "petal_length", "petal_width"]].mean())


# STEP 4. Generate and save variable summaries to a text file.

# Create summary for numerical variables (float64)
numerical_summary = df.describe(include=[np.number]) # 'Sepal length', 'sepal width', 'petal length', 'petal width' variables

# Create summary for categorical variables (object)
categorical_summary = df.describe(include=[object]) # 'Species' variable

# Write the summaries to a text file
with open('Summary_variable.txt', 'w') as file:
    file.write("Numerical Variables Summary:\n")
    file.write(numerical_summary.to_string())
    file.write("\n\nCategorical Variables Summary:\n")
    file.write(categorical_summary.to_string())

# STEP 5. Creating a Histogram for each variable.

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

# STEP 6. Creating a Scatter plot of each of pair of variables taking into account types of species.

# Scatter Plot 1: Sepal Length vs Sepal Width.

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

# Scatter Plot 2: Petal Length vs Petal Width.

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

# Scatter plot 3: Sepal Length vs Petal Length

# Extract data for sepal length, petal length and species.
sepallen = df['sepal_length']
petallen = df['petal_length']
spe = df['species'].unique()

# Define colors and markers for each species in the plot
colors = ['indigo', 'green', 'yellow']  # Different colors for categorize Iris
markers = ['o', '^', 's']          # Different markers for categorize Iris

# Create scatter plot for each species
plt.figure(figsize=(10, 8))
for i, species in enumerate(spe):
    species_data = df[df['species'] == species]
    plt.scatter(species_data['sepal_length'], species_data['petal_length'], color=colors[i], marker=markers[i], label=species, alpha=0.7)

# Decorative details in the plot
plt.title('Scatter Plot of Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.legend()
# Save the plot to a file (in this case png file)
plt.savefig('Sepal_Length_Petal_Length_Scatter_Plot.png')
# Show the plot.
plt.show()

# Scatter plot 4: Sepal Length vs Petal Width

# Extract data for sepal length, petal width and species.
sepallen = df['sepal_length']
petalwd = df['petal_width']
spe = df['species'].unique()

# Define colors and markers for each species in the plot
colors = ['indigo', 'green', 'yellow']  # Different colors for categorize Iris
markers = ['o', '^', 's']          # Different markers for categorize Iris

# Create scatter plot for each species
plt.figure(figsize=(10, 8))
for i, species in enumerate(spe):
    species_data = df[df['species'] == species]
    plt.scatter(species_data['sepal_length'], species_data['petal_width'], color=colors[i], marker=markers[i], label=species, alpha=0.7)

# Decorative details in the plot
plt.title('Scatter Plot of Sepal Length vs Petal Width by Species')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Width')
plt.legend()
# Save the plot to a file (in this case png file)
plt.savefig('Sepal_Length_Petal_Width_Scatter_Plot.png')
# Show the plot.
plt.show()

# Scatter plot 5: Sepal Width vs Petal Length

# Extract data for sepal width, petal length and species.
sepallen = df['sepal_width']
petallen = df['petal_length']
spe = df['species'].unique()

# Define colors and markers for each species in the plot
colors = ['indigo', 'green', 'yellow']  # Different colors for categorize Iris
markers = ['o', '^', 's']          # Different markers for categorize Iris

# Create scatter plot for each species
plt.figure(figsize=(10, 8))
for i, species in enumerate(spe):
    species_data = df[df['species'] == species]
    plt.scatter(species_data['sepal_width'], species_data['petal_length'], color=colors[i], marker=markers[i], label=species, alpha=0.7)

# Decorative details in the plot
plt.title('Scatter Plot of Sepal Width vs Petal Length by Species')
plt.xlabel('Sepal Width')
plt.ylabel('Petal Length')
plt.legend()
# Save the plot to a file (in this case png file)
plt.savefig('Sepal_Width_Petal_Length_Scatter_Plot.png')
# Show the plot.
plt.show()

# Scatter plot 6: Sepal Width vs Petal Width

# Extract data for sepal width, petal width and species.
sepallen = df['sepal_width']
petallen = df['petal_width']
spe = df['species'].unique()

# Define colors and markers for each species in the plot
colors = ['indigo', 'green', 'yellow']  # Different colors for categorize Iris
markers = ['o', '^', 's']          # Different markers for categorize Iris

# Create scatter plot for each species
plt.figure(figsize=(10, 8))
for i, species in enumerate(spe):
    species_data = df[df['species'] == species]
    plt.scatter(species_data['sepal_width'], species_data['petal_width'], color=colors[i], marker=markers[i], label=species, alpha=0.7)

# Decorative details in the plot
plt.title('Scatter Plot of Sepal Width vs Petal Width by Species')
plt.xlabel('Sepal Width')
plt.ylabel('Petal Width')
plt.legend()
# Save the plot to a file (in this case png file)
plt.savefig('Sepal_Width_Petal_Width_Scatter_Plot.png')
# Show the plot.
plt.show()


# STEP 7: Measure correlation coefficient.

# Calculate correlation coefficient for all pairwise combinations.
# Exclude all categorical (non-numeric) variables for correlation calculation, in this case 'Species' (object).
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Calculate correlation matrix.
correlation_matrix = numeric_df.corr().round (2) # rounding correlation matrix to 2 digits.
# Print correlation matrix.
print(correlation_matrix)


# Heat map.
# Generate a Heatmap to visualize the correlation matrix with all values obtained.
sns.heatmap(correlation_matrix, cmap='RdPu', annot=True) #annot=True are numeric values annotations onto heatmap cells. 
# Adding Heat map tittle
plt.title('Heatmap Correlation Matrix')
# Save the plot to a file (in this case png file)
plt.savefig('Correlation_matrix_Heatmap.png')
# Show plot
plt.show()



# End