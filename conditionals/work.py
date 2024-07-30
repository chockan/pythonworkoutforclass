# a = int(input("enter the value"))
# if a > 18:
#     print(a, "is greater")
# print("done")

###########################################
# a=int(input('enter the number'))
# if a>=18:
#     print("a is greater")
# else:
#     print("a is smaller than the input given")

####################################################

# a=int(input('enter the number'))
# b=int(input('enter the number'))
# c=int(input('enter the number'))
# if a>b:

#     print("a is greater")
# elif b>c:
#     print("b is greater")
# else:
#     print("c is greater")

#################################################
# var = 100
# if var == 200:
#     print("1 - Got a true expression value")
#     print(var)
# elif var == 150:
#     print("2 - Got a true expression value")
#     print(var)
# elif var == 100:
#     print("3 - Got a true expression value")
#     print(var)
# else:
#     print("4 - Got a false expression value")
#     print(var)
# print("Good bye!")

##################################################
# num = int(input("Enter the value of num: "))
# if (num < 0):
#   print("Number is negative.")
# elif (num == 0):
#   print("Number is Zero.")
# elif (num == 999):
#   print("Number is Special.")
# else:
#   print("Number is positive.")

# print("I am happy now")

###################################################

# num = 18
# if (num < 0):
#     print("Number is negative.")
# elif (num > 0):
#     if (num <= 10):
#         print("Number is between 1-10")
#     elif (num > 10 and num <= 20):
#         print("Number is between 11-20")
#     else:
#         print("Number is greater than 20")
# else:
#     print("Number is zero")

#################################################

# name = 'Abhishek'
# for i in name:
#     print(i,end="")
# print()

# #################################################
# name = 'Abhishek'
# for i in name:
#     print(i, end=" ")

################################################

# num1 = float(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ")
# num2 = float(input("Enter second number: "))

# if operator == '+':
#     print("Result:", num1 + num2)
# elif operator == '-':
#     print("Result:", num1 - num2)
# elif operator == '*':
#     print("Result:", num1 * num2)
# elif operator == '/':
#     if num2 != 0:
#         print("Result:", num1 / num2)
#     else:
#         print("Error: Division by zero!")
# else:
#     print("Invalid operator!")

################################################
# temperature = float(input("Enter temperature: "))
# scale = input("Enter scale (C for Celsius, F for Fahrenheit): ")

# if scale.upper() == 'C':
#     converted_temp = (temperature * 9/5) + 32
#     print("Converted temperature:", converted_temp, "F")
# elif scale.upper() == 'F':
#     converted_temp = (temperature - 32) * 5/9
#     print("Converted temperature:", converted_temp, "C")
# else:
#     print("Invalid scale!")

###############################################
# numbers = [1, 2, 4, 6, 11, 20]
# seq=0
# for val in numbers:
#     seq=val*val
#     print(seq)
###########################################
college = {"ces":"block1","it":"block2","ece":"block3"}
# #Iterating over the dictionary to print keys
# print ('Keys are:')
for keys in college:
    print (keys)
# #Iterating over the dictionary to print values
# print ('Values are:')
for blocks in college.values():
    print(blocks)


########################################
info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info) 
# print(info.keys())
# print(info.values())

# for key in info.keys():
#   print(f"The value corresponding to the key {key} is {info[key]}")

# print(info.items())
for a, b in info.items():
    print(a,b)
  #print(f"The value corresponding to the key {a} is {b}")

##################################################################
colors = ["Red", "Green"]

for color in colors:
  print(color)
  for i in color:
    print(i)

#################################################################

for i in range(1,6):
    for j in range(0,i):
        print(i, end=" ")
    print()


###########################################################
names = ["Dave", "Sara", "John"]
for x in names:
    print(x)

for x in "Mississippi":
    print(x)

for x in names:
    if x == "Sara":

        break
    print(x)

for x in names:
    if x == "Sara":
        continue
    print(x)

for x in range(4):
    print(x)

for x in range(2, 4):
    print(x)

################################################################

count = 5
while (count > 0):
  print(count)
  count = count - 1
else:
  print("I am inside else")

##############################################################

def hf():
    print("hw")
    print("gh kfjg 66666")
hf()
hf()
hf()


##############################################
# def add(x,y):
#     c=x+y
#     return c
# print(add(5,4))

#########################################3