def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

def isLesser(a, b):
  pass
  

a = 9
b = 8
isGreater(a, b)
calculateGmean(a, b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)
c = 8
d = 74
isGreater(c, d)
calculateGmean(c, d)
# gmean2 = (c*d)/(c+d)
# print(gmean2)


### Default arguments:
#We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.


def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")



##example
# def average(a, b, c=1):
#   print("The average is ", (a + b + c) / 2)


def average(*numbers):
  # print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  # print("Average is: ", sum / len(numbers))
  # return 7
  return sum / len(numbers)


# average(4, 6)
# average(b=9)

c = average(5, 6, 7, 1)
print(c)

#examples
#############################################
def name(**name):
  # print(type(name))
  print("Hello,", name["fname"], name["mname"], name["lname"])


name(mname="Buchanan", lname="Barnes", fname="James")
##################################################
#example
def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("Dave", "John", "Sara")
#########################################################
##examples

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_named_items(first="Dave", last="Gray")
##########################################################

##examples
##BMI CALCULATOR

# BMI calculator
name1 = "YK"
height_m1 = 2
weight_kg1 = 90

name2 = "YK's sister"
height_m2 = 1.8
weight_kg2 = 70

name3 = "YK's brother"
height_m3 = 2.5
weight_kg3 = 160

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"
result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)
print(result1)
print(result2)
print(result3)
#################################################