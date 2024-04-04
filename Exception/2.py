try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError as e:
    # Handle the specific exception
    print(f"Error: {e}")


##################################################
    
# Handling Multiple Exceptions

# Python allows handling multiple exceptions in a single try-except block.

try:
    # Code that may raise different exceptions
    result = int("text")
except (ValueError, TypeError) as e:
    # Handle both Value and Type errors
    print(f"Error: {e}")

#######################################################
try:
   f = open("data.txt")
   num = int(input("Enter a number: "))
   value = 10 / num

except FileNotFoundError:
   print("The file was not found!")
   
except ValueError:
   print("Please enter a number.")
   
except ZeroDivisionError:
   print("Cannot divide by zero!")
    
#########################################################
   
try:
    # Code that may raise an exception
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division successful")
finally:
    print("This will always be executed")
   
########################################################
def f():
    x = int("four")

try:
    f()
except ValueError as e:
    print("got it :-) ", e)


print("Let's get on")
    
#########################################################
    
# Python code to illustrate working of try-except
try:
    x=int(input("Enter a number:" ))
    y=int(input("Enter another number:" ))
    result = x // y # Floor Division : Gives only fractional part as answer
    print("Yeah ! Your answer is : result")
except ZeroDivisionError:
    print("Sorry ! Cannot divide by zero")
    

########################################################
try:
    # Code that may raise an exception
    result = open("file.txt", "r").read()
except FileNotFoundError as e:
    # Handle file not found error
    print(f"Error: {e}")
finally:
    # Cleanup operations, e.g., closing files or releasing resources
    print("Execution complete.")

############################################################
    
# Python program to demonstrate try-except-else-finally
try:
    x=int(input("Enter a number:" ))
    y=int(input("Enter another number:" ))
    z=x/y # can raise divide by zero exception 
    print("Your answer is :", z)
except ZeroDivisionError:
    # handles zerodivision exception      
    print("Cannot divide by zero")
else:
    #prints if try block executes
    print("The division was successful")
finally:
    # this block executes regardless of exception generation
    print("Have a good day")
    


############################################################
#Custom Exceptions

#Developers can create custom exceptions by defining new classes. This adds clarity and specificity to error handling.

class CustomError(Exception):
    def __init__(self, message="A custom error occurred."):
        self.message = message
        super().__init__(self.message)

try:
    raise CustomError("This is a custom exception.")
except CustomError as ce:
    print(f"Custom Error: {ce}")