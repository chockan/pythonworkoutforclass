# One-dimensional array
one= [1, 2, 3, 4, 5]


print(one_dimensional_array[0])  # Output: 1
print(one_dimensional_array[2])  # Output: 3


# Two-dimensional array (matrix) using nested lists
two_dimensional_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print(two_dimensional_array[0][1])  # Output: 2
print(two_dimensional_array[2][2])  # Output: 9

##########################################
import numpy as np

# One-dimensional array
one_d_array = np.array([1, 2, 3, 4, 5])

# Two-dimensional array (matrix)
two_d_array = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Accessing elements
print(one_d_array[2])       # Output: 3
print(two_d_array[0, 1])    # Output: 2
print(two_d_array[2, 2])    # Output: 9
