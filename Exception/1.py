# The try: block contains statements which are susceptible for exception

# If exception occurs, the program jumps to the except: block.

# If no exception in the try: block, the except: block is skipped.


# syntax
# try:
#    You do your operations here
# #    ......................
# except ExceptionI:
# #    If there is ExceptionI, then execute this block.
# except ExceptionII:
# #    If there is ExceptionII, then execute this block.
#    ......................
# else:
# #    If there is no exception then execute this block.


# importance of Exception Handling in PythonException handling plays a pivotal role in enhancing the reliability and maintainability of Python code. Here’s why it’s crucial:Error Identification

# Why it matters:  Exception handling allows you to identify errors quickly and accurately.
# Best practice:  Implement precise error messages to facilitate troubleshooting.
# Graceful Error Recovery

# Why it matters: Instead of crashing, well-handled exceptions enable graceful recovery from errors.
# Best practice: Use try-except blocks to manage errors and provide fallback mechanisms.
# Code Readability

# Why it matters: Properly handled exceptions contribute to clean and readable code.
# Best practice: Focus on clarity and specificity when handling different types of exceptions.


# Different types of Exceptions in Python
# In Python, exceptions are events that occur during the execution of a program that disrupts the normal flow of instructions. Here are some common types of exceptions in Python:

# SyntaxError:

# Raised when there is a syntax error in the code, indicating a mistake in the program’s structure.
# # Example SyntaxError
# print("Hello World"  # Missing closing parenthesis
# IndentationError:

Raised when there is an issue with the indentation of the code. Python relies on proper indentation to define blocks of code.
# Example IndentationError
if True:
print("Indented incorrectly")  # Missing indentation
TypeError:

Raised when an operation or function is applied to an object of an inappropriate type.
# Example TypeError
num = "5"
result = num + 2  # Trying to concatenate a string with an integer
ValueError:

Raised when a built-in operation or function receives an argument with the correct type but an inappropriate value.
# Example ValueError
num = int("abc")  # Attempting to convert a non-numeric string to an integer
NameError:
Raised when an identifier (variable or function name) is not found in the local or global namespace.
# Example NameError
print(undefined_variable)  # Variable is not defined
IndexError:

Raised when trying to access an index that is outside the bounds of a sequence (e.g., list, tuple, string).
# Example IndexError
my_list = [1, 2, 3]
print(my_list[5])  # Accessing an index that doesn't exist
KeyError:

Raised when trying to access a dictionary key that does not exist.
# Example KeyError
my_dict = {"name": "John", "age": 25}
print(my_dict["gender"])  # Accessing a key that is not in the dictionary
FileNotFoundError:

Raised when attempting to open a file that does not exist.
# Example FileNotFoundError
with open("nonexistent_file.txt", "r") as file:
    content = file.read() 











def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_named_items(first="Dave", last="Gray")


