
#example1
def hf():
    print("hw")
    print("gh kfjg 66666")
hf()
hf()
hf()

#example
def hello_f():
    return "hellocollege"
print(hello_f().upper())

#example
def add(x,y):
    c=x+y
    return c
print(add(5,4))
#example
def add(x,y):
    c=x+y
    print(c)
add(5,4)

#example
def wish(name,msg):

    print("Hello",name + ' ' + msg)
wish("MRCET","Good morning!")
#example
def hello(wish, hello):

    return f"hi {wish},{hello}"

print(hello("mrcet", "college"))

#example
def hello(wish, hello):
    return "hi {},{}".format(wish, hello)

print(hello("mrcet", "college"))

#example
def sum(a=4, b=2): #2 is supplied as default argument

    print (a+b)
sum(1,2) #calling with arguments
sum( ) #calling without arguments
#example
def wish(*names):

    for name in names:
        print("Hello",name)
wish("MRCET","CSE","SIR","MADAM")

#example
#Program to find area of a circle using function use single return value function with
#argument.
pi=3.14
def areaOfCircle(r):
    return pi*r*r
r=int(input("Enter radius of circle"))
print(areaOfCircle(r))

#example
#Program to write sum different product and using arguments with return value
#function.
def calculete(a,b):
    total=a+b
    diff=a-b
    prod=a*b
    div=a/b
    mod=a%b

    return total,diff,prod,div,mod
a=int(input("Enter a value"))
b=int(input("Enter b value"))
#function call
s,d,p,q,m = calculete(a,b)
print("Sum= ",s)
print("diff= ",d)
print("mul= ",p)
print("div= ",q)
print("mod= ",m)

#example
#program to find biggest of two numbers using functions.
def biggest(a,b):
    if a>b :
        return a
    else :
        return b
a=int(input("Enter a value"))
b=int(input("Enter b value"))
#function call
big= biggest(a,b)
print("big number= ",big)

#example
#program to find biggest of two numbers using functions. (nested if)
def biggest(a,b,c):
    if a>b :
        if a>c :
            return a
        else :
            return c
    else :
        if b>c :
            return b
        else :
            return c
a=int(input("Enter a value"))
b=int(input("Enter b value"))
c=int(input("Enter c value"))
#function call
big= biggest(a,b,c)
print("big number= ",big)

#example
#Writer a program to read one subject mark and print pass or fail use single return
#values function with argument.
def result(a):
    if a>40:
        return "pass"
    else:
        return "fail"
a=int(input("Enter one subject marks"))
print(result(a))

#example
#Write a program to display mrecet cse dept 10 times on the screen. (while loop)
def usingFunctions():
    count =0
    while count<10:
        print("mrcet cse dept",count)
        count=count+1
usingFunctions()

##example
def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2


total = sum(7, 2)
print(total)

