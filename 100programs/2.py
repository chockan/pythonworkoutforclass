
# Question 1
# Level 1
# Question:
# Write a program which will find all such numbers which are divisible by 7 but 
are not a multiple of 5,between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# Hints: 
# Consider use range(#begin, #end) method
# Solution:

l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))
print(','.join(l))


Question 2
# Level 1
# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input

def fact(x):
 if x == 0:
    return 1
    return x * fact(x - 1)
x=int(raw_input())
print(fact(x))

#----------------------------------------#
#----------------------------------------#
 Question 3
# Level 1
# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# Hints:
# In case of input data being supplied to the question, it should be assumed to 
# be a console input.
# Consider use dict()

# Solution:
n=int(raw_input())
d=dict()
for i in range(1,n+1):
 d[i]=i*i
print(d)

#----------------------------------------#
#----------------------------------------#
#Question 4
# Level 1
# Question:
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
# Hints:
# In case of input data being supplied to the question, it should be assumed to 
# be a console input.
# tuple() method can convert list to tuple
# Solution:

values=input()
l=values.split(",")
t=tuple(l)
print(l)
print(t)

#Question 5
# Level 2
# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-
# dimensional array. The element value in the i-th row and j-th column of the array 
# should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
# Hints:
# Note: In case of input data being supplied to the question, it should be 
# assumed to be a console input in a comma-separated form.
# Solution:


input_str = input()
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col
        print(multilist)

#----------------------------------------#
#----------------------------------------#
# Question 6
# Level 2
# Question£º
# Write a program that accepts sequence of lines as input and prints the lines 
# after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
# Hints:
# In case of input data being supplied to the question, it should be assumed to 
# be a console input.
# Solution:
lines = []
while True:
    s = raw_input()
    if s:
        lines.append(s.upper())
    else:
        break
for sentence in lines:
 print(sentence)

#----------------------------------------#
#----------------------------------------#
# Question 7
# Level 2
# Question:
# Write a program which accepts a sequence of comma separated 4 digit 
# binary numbers as its input and then check whether they are divisible by 5 or not. 
# The numbers that are divisible by 5 are to be printed in a comma separated 
# sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
# Hints:
# In case of input data being supplied to the question, it should be assumed to 
# be a console input.
# Solution:
value = []
items=[x for x in raw_input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)
        print(','.join(value))