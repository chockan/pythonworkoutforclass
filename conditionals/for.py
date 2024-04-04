numbers = [1, 2, 4, 6, 11, 20]
seq=0
for val in numbers:
    seq=val*val
    print(seq)

###########################################
list = ['M','R','C','E','T']
i = 1
#Iterating over the list
for item in list:
    print ('college ',i,' is ',item)
    i = i+1

#########################################
    
tuple = (2,3,5,7)
print ('These are the first four prime numbers ')
#Iterating over the tuple
for a in tuple:
    print (a)

#############################################
#creating a dictionary
college = {"ces":"block1","it":"block2","ece":"block3"}
#Iterating over the dictionary to print keys
print ('Keys are:')
for keys in college:
    print (keys)
#Iterating over the dictionary to print values
print ('Values are:')
for blocks in college.values():
    print(blocks)

#####################################################
# Example 1 of Nested For Loops (Pattern Programs)
for i in range(1,6):
    for j in range(0,i):
        print(i, end=" ")
    print('')
####################################################

# Example 2 of Nested For Loops (Pattern Programs)
for i in range(1,6):
    for j in range(5,i-1,-1):
        print(i, end=" ")
    print('')

#################################################
for val in "MRCET COLLEGE":
    if val == " ":
        break
    print(val)
print("The end")

######################################################
# Program to display all the elements before number 88
for num in [11, 9, 88, 10, 90, 3, 19]:
    print(num)
    if(num==88):
        print("The number 88 is found")
        print("Terminating the loop")
        break

#########################################################
for letter in "Python": # First Example
    if letter == "h":
        break
    print("Current Letter :", letter )
#########################################################

# Program to show the use of continue statement inside loops
for val in "string":
    if val == "i":
        continue
    print(val)
print("The end")

#####################################################

# program to display only odd numbers
for num in [20, 11, 9, 66, 4, 89, 44]:
# Skipping the iteration when number is even
    if num%2 == 0:
        continue
# This statement will be skipped for all even numbers
    print(num)

#######################################################
for letter in "Python": # First Example
    if letter == "h":
        continue
    print("Current Letter :", letter)

#########################################################

sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass

#######################################
name = 'Abhishek'
for i in name:
  print(i)
  if(i =="b"):
    print("This is something special!")
    
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
  print(color)
  for i in color:
    print(i)

for k in range(5):
  print(k + 1)
  
for k in range(1, 20001):
  print(k)

  
for k in range(1, 12, 3):
  print(k)


#########################################
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
#########################################
for x in range(5, 101, 5):
    print(x)
else:
    print("Glad that\'s over!")

names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

for name in names:
    for action in actions:
        print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")
############################################


