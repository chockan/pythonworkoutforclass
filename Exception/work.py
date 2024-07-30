# try:
#     # Code that may raise an exception
#     result = 10 / 0
# except ZeroDivisionError :
#     # Handle the specific exception
#     # print(f"Error: {e}")
#     print("error")
# else:
#     print("no error")


############################################
# try:
#     # Code that may raise different exceptions
#     result = int(input("enter value:"))
    
# except :
#     # Handle both Value and Type errors
#     print("Error")
# else:
#     print("no error")

###############################################
try:
   f = open("d:/python course/new5.txt")
   num = int(input("Enter a number: "))
   value = 10 / num

except FileNotFoundError:
   print("The file was not found!")
   
except ValueError:
   print("Please enter a number.")
   
except ZeroDivisionError:
   print("Cannot divide by zero!")

except:
   print("error")
else:
   print("no error")

finally:
   print("completed")

###################################################