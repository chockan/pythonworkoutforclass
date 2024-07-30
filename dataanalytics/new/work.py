import pandas as pd

# Creating a Series from a list
s = pd.Series([1, 2, 3, 4, 5])
print(s)
print(type(s))

#########################################
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)

