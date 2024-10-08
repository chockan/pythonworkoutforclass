""" 

> **_Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
> between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line._**

"""

l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l))


##############
for i in range(2000,3201):
    if i%7 == 0 and i%5!=0:
        print(i,end=',')
print("\b")

##########
print(*(i for i in range(2000, 3201) if i%7 == 0 and i%5 != 0), sep=",")

##########
""" 
_Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8
> Then, the output should be:40320_**
"""
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x = int(input())
print(fact(x))

####################
n = int(input()) #input() function takes input as string type
                   #int() converts it to integer type
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i = i + 1
print(fact)

############
n = int(input()) #input() function takes input as string type
                  #int() converts it to integer type
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)
##############

n = int(input())
def shortFact(x): return 1 if x <= 1 else x*shortFact(x-1)
print(shortFact(n))

##########
while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError as err:
        print(err)

org = num
fact = 1
while num:
    fact = num * fact
    num = num - 1
print(f'the factorial of {org} is {fact}')

############
from functools import reduce

def fun(acc, item):
	return acc*item

num = int(input())
print(reduce(fun,range(1, num+1), 1))

###########

""" 
_With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8_**

> **_Then, the output should be:_**

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


### Hints:

> **_In case of input data being supplied to the question, it should be assumed to be a console input.Consider use dict()_**
"""

n = int(input())
d = dict()
for i in range(1,n+1):
    d[i] = i * i
print(d)
##############
n = int(input())
ans = {}
for i in range (1,n+1):
    ans[i] = i * i
print(ans)

#############
n = int(input())
ans={i : i*i for i in range(1,n+1)}
print(ans)

#############

try:
    num = int(input("Enter a number: "))
except ValueError as err:
    print(err)

dictio = dict()
for item in range(num+1):
    if item == 0:
        continue
    else:
	    dictio[item] = item * item
print(dictio)

#################
num = int(input("Number: "))
print(dict(enumerate([i*i for i in range(1, num+1)], 1)))

  