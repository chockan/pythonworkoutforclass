# 100+ Python challenging programming exercises
# 1. Level description
# Level Description
# Level 1 Beginner means someone who has just gone through an 
# introductory Python course. He can solve some problems with 1 or 2 Python 
# classes or functions. Normally, the answers could directly be found in the 
# textbooks.
# Level 2 Intermediate means someone who has just learned Python, but 
# already has a relatively strong programming background from before. He should 
# be able to solve problems which may involve 3 or 3 Python classes or functions. 
# The answers cannot be directly be found in the textbooks.
# Level 3 Advanced. He should use Python to solve more complex problem 
# using more rich libraries functions and data structures and algorithms. He is 
# supposed to solve the problem using several Python standard packages and 
# advanced techniques.
# 2. Problem template
# #----------------------------------------#
# Question
# Hints
# Solution
# 3. Questions
#----------------------------------------#
# Question 1
# Level 1
# Question:
# Write a program which will find all such numbers which are divisible by 7 but 
# are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on 
# a single line.
# Hints: 
# Consider use range(#begin, #end) method
# Solution:
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))
print(','.join(l))
#----------------------------------------#
#----------------------------------------#
# Question 2
# Level 1
# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single 
# line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
# Hints:
# In case of input data being supplied to the question, it should be assumed to 
# be a console input.
#Solution:
def fact(x):
 if x == 0:
    return 1
    return x * fact(x - 1)
x=int(input())
print(fact(x))
#----------------------------------------#
#----------------------------------------#
# Question 3
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
n=int(input())
d=dict()
for i in range(1,n+1):
 d[i]=i*i
print(d)
#----------------------------------------#
#----------------------------------------#
# Question 4
# Level 1
# Question:
# Write a program which accepts a sequence of comma-separated numbers 
# from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
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
#----------------------------------------#
#----------------------------------------#
# Question 5
# Level 1
# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
# Hints:
# Use __init__ method to construct some parameters
# Solution:
class InputOutString(object):
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input()
    def printString(self):
        print(self.s.upper())
strObj = InputOutString()
strObj.getString()
strObj.printString()
#----------------------------------------#
#----------------------------------------#
# Question 6
# Level 2
# Question:
# Write a program that calculates and prints the value according to the given 
# formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a commaseparated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the 
# program:
# 100,150,180
# The output of the program should be:
# 18,22,24
# Hints:
# If the output received is in decimal form, it should be rounded off to its 
# nearest value (for example, if the output received is 26.0, it should be printed as 
# 26)
# In case of input data being supplied to the question, it should be assumed to 
# be a console input. 
# Solution:
#!/usr/bin/env python
import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
 value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print(','.join(value))
#----------------------------------------#
#----------------------------------------#
# Question 7
# Level 2
# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-
# dimensional array. The element value in the i-th row and j-th column of the array 
# should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡Y-1.
# Exampleinput
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
# Question 8
# Level 2
# Question:
# Write a program that accepts a comma separated sequence of words as input 
# and prints the words in a comma-separated sequence after sorting them 
# alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world
# Hints:
# In case of input data being supplied to the question, it should be assumed to 
# be a console input.
# Solution:
items=[x for x in input().split(',')]
items.sort()
print(','.join(items))
#----------------------------------------#
#----------------------------------------#
# Question 9
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
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break
for sentence in lines:
 print(sentence)
#----------------------------------------#
#----------------------------------------#
# Question 10
# Level 2
# Question:
# Write a program that accepts a sequence of whitespace separated words as 
# input and prints the words after removing all duplicate words and sorting them 
# alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world
# Hints:
# In case of input data being supplied to the question, it should be assumed to 
# be a console input.
# We use set container to remove duplicated data automatically and then use 
# sorted() to sort the data.
# Solution:
s = input()
words = [word for word in s.split(" ")]
print(" ".join(sorted(list(set(words)))))
#----------------------------------------#
#----------------------------------------#
# Question 11
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
items=[x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)
        print(','.join(value))
#----------------------------------------#
#----------------------------------------#
# Question 12
# Level 2
# Question:
# Write a program, which will find all such numbers between 1000 and 3000 
# (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on 
# a single line.
# Hints:
# In case of input data being supplied to the question, it should be assumed to 
# be a console input.
# Solution:
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])
%2==0):
        values.append(s)
        print(",".join(values))
#----------------------------------------#
# #----------------------------------------#
# Question 13
# Level 2
# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
# Hints:
# In case of input data being supplied to the question, it should be assumed to 
# be a console input.
# Solution:
s = input()
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])
#--------------------