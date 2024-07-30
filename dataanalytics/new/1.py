"""
Series:
A Series is a one-dimensional labeled array capable of holding data of any type (integer, float, string, Python objects, etc.). It is similar to a one-dimensional array or a column in a table. Each element in a Series has a unique label, known as its index.

Key Characteristics of a Series:
Homogeneous Data: A Series contains elements of the same data type.
Indexing: Each element in a Series has an associated label, which can be used for indexing and accessing data.
Size Immutable: The size of a Series is fixed upon creation.
Label Persistence: Labels are preserved during operations, even if the result has missing elements.

import pandas as pd

# Creating a Series from a list
s = pd.Series([1, 2, 3, 4, 5])
print(s)

#output
0    1
1    2
2    3
3    4
4    5
dtype: int64
#########################################################################
DataFrame:
A DataFrame is a two-dimensional labeled data structure with columns of potentially different data types. 
It is like a spreadsheet or SQL table, where data is arranged in rows and columns. 
Each column in a DataFrame is a Series.

Key Characteristics of a DataFrame:
Heterogeneous Data: A DataFrame can contain columns of different data types.
Indexing: Like Series, DataFrames have both row and column labels, allowing for flexible indexing and slicing.
Tabular Structure: DataFrames are tabular data structures, making them suitable for representing structured data.
Size Mutable: DataFrames can be resized, columns can be inserted, deleted, or modified.

########
import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)
#output
      Name  Age         City
0    Alice   25     New York
1      Bob   30  Los Angeles
2  Charlie   35      Chicago


"""