#Subsetting Arrays (Using numpy):

import numpy as np

# Creating a numpy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Subsetting rows and columns
subset1 = arr[0]  # Selecting the first row
subset2 = arr[:, 1]  # Selecting the second column
subset3 = arr[1:, :2]  # Selecting a sub-matrix excluding the first row and beyond the second column

print("Subset 1:", subset1)
print("Subset 2:", subset2)
print("Subset 3:\n", subset3)

# Calculating statistics
mean = np.mean(arr)  # Calculate the mean of all elements
max_value = np.max(arr)  # Find the maximum value
min_value = np.min(arr)  # Find the minimum value
sum_values = np.sum(arr)  # Calculate the sum of all elements

print("Mean:", mean)
print("Max:", max_value)
print("Min:", min_value)
print("Sum:", sum_values)


##################################################################
#Subsetting DataFrames (Using pandas):

import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Salary': [50000, 60000, 70000, 80000]}
df = pd.DataFrame(data)

# Subsetting rows and columns
subset1_df = df[df['Age'] > 30]  # Selecting rows where Age is greater than 30
subset2_df = df[['Name', 'Salary']]  # Selecting specific columns

print("Subset 1:")
print(subset1_df)
print("\nSubset 2:")
print(subset2_df)



# Descriptive statistics
summary_stats = df.describe()  # Generates descriptive statistics of numerical columns
unique_names = df['Name'].unique()  # Get unique values in the 'Name' column
value_counts = df['Age'].value_counts()  # Count occurrences of each value in the 'Age' column

print("Summary statistics:")
print(summary_stats)
print("\nUnique names:", unique_names)
print("\nValue counts for Age:")
print(value_counts)


######################################################################

