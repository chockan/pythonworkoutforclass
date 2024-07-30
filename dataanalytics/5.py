"""

Subsetting methods in Python are techniques used to extract specific portions or elements from data structures like lists, arrays, dictionaries, and DataFrames. Subsetting allows you to focus on relevant parts of your data for analysis or manipulation. Here are some common subsetting methods in Python:

Lists:
Lists are one-dimensional arrays that can hold elements of different data types.

Basic Subsetting:
python
Copy code
my_list = [1, 2, 3, 4, 5]

# Accessing individual elements
element = my_list[0]  # Accessing the first element

# Slicing to extract a sublist
sublist = my_list[2:4]  # Extract elements from index 2 to 3 (exclusive)
Arrays (Using numpy):
Numpy arrays are multi-dimensional arrays used for numerical computing.

Basic Subsetting:
python
Copy code
import numpy as np

my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Accessing individual elements
element = my_array[0, 1]  # Accessing the element in the first row and second column

# Slicing to extract a sub-array
subarray = my_array[:, 1:]  # Extracting columns starting from index 1
Dictionaries:
Dictionaries are unordered collections of key-value pairs.

Basic Subsetting:
python
Copy code
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Accessing values using keys
value = my_dict['age']  # Accessing the value associated with the key 'age'
DataFrames (Using pandas):
DataFrames are two-dimensional labeled data structures with columns of potentially different types.

Basic Subsetting:
python
Copy code
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}
df = pd.DataFrame(data)

# Accessing columns
column = df['Age']  # Accessing the 'Age' column

# Accessing rows based on conditions
subset = df[df['Age'] > 30]  # Selecting rows where Age is greater than 30

"""