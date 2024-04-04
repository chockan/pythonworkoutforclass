
def divide(x, y):
      try:
             res = x / y
             print('Your answer is :', res)
      except ZeroDivisionError:
             print('Sorry! You are dividing by zero')

divide(5, 0)

###################################################################


try:
    num1 = input('Enter 1st number: ')
    num2 = input('Enter 2nd number: ')
    result = (int(num1) * int(num2))/(10 * int(num2))
except ValueError as ve:
    print(ve)
    exit()
except ZeroDivisionError as zde:
    print(zde)
    exit()
except TypeError as te:
    print(te)
    exit()
except:
    print('Unexpected Error!')
    exit()

print(result)


#############################################################
