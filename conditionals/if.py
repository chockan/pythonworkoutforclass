a = 3
if a > 2:
    print(a, "is greater")
print("done")

####################################
a = -1
if a < 0:
    print(a, "a is smaller")
print("Finish")

##################################
#Example of if - else:
a=int(input('enter the number'))
if a>5:
    print("a is greater")
else:
    print("a is smaller than the input given")

################################
a=10
b=20
if a>b:
    print("A is Greater than B")
else:
    print("B is Greater than A")

###################################
    
a=int(input('enter the number'))
b=int(input('enter the number'))
c=int(input('enter the number'))
if a>b:

    print("a is greater")
elif b>c:
    print("b is greater")
else:
    print("c is greater")

#################################
    
var = 100
if var == 200:
    print("1 - Got a true expression value")
    print(var)
elif var == 150:
    print("2 - Got a true expression value")
    print(var)
elif var == 100:
    print("3 - Got a true expression value")
    print(var)
else:
    print("4 - Got a false expression value")
    print(var)
print("Good bye!")

#########################################

a = int(input("Enter your age: "))
print("Your age is:", a)
# Conditional operators 
# >, <, >=, <=, ==, !=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)
if(a>18):
  print("You can drive")
  print("Yes")
else:
  print("You cannot drive")
  print("No")
  print("Yay!")

############################################
num = int(input("Enter the value of num: "))
if (num < 0):
  print("Number is negative.")
elif (num == 0):
  print("Number is Zero.")
elif (num == 999):
  print("Number is Special.")
else:
  print("Number is positive.")

print("I am happy now")

################################################
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

##############################################
g = 9
h = 8
if g < h:
    print("g is less than h")
else:
    if g == h:
        print("g is equal to h")
    else:
        print("g is greater than h")

#################################################
e = 20
f = 8
if e < f:
    print("e is less than f")
elif e == f:
    print("e is equal to f")
elif e > f + 10:
    print("e is greater than f by more than 10")
else:
    print("e is greater than f")
