class InvalidInputError(Exception):
   pass

num = int(input("Please enter a number: "))

if num < 0:
   raise InvalidInputError("Number cannot be negative!")

##############################################################

class InvalidInputError(Exception):
   pass
try:
   num = int(input("Please enter a number: "))
   if num < 0:
      raise InvalidInputError("Negative number not allowed!")
except InvalidInputError as e:
    print(e)

##################################################################
class NegativeNumberError(Exception):
   pass
   
def calculate_square(num):
   if num < 0:
      raise NegativeNumberError("Negative numbers unacceptable")
   return num**2

num = -6   
try:
   result = calculate_square(num)
except NegativeNumberError as e:
   print(e)