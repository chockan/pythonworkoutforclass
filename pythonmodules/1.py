# write a python program to display date
import datetime
a=datetime.date(2000,9,18)
print(a)
#Output:
#2000-09-18

###############################
# write a python program to display time
import datetime
a=datetime.time(5,3)
print(a)
#Output:
#5:03:00
##################################################

#write a python program to print date, time for today and now.
import datetime

a=datetime.datetime.today()
b=datetime.datetime.now()
print(a)
print(b)
#Output:
#2019-11-29 12:49:52.2355818
#2019-11-29 12:49:52.2355818

###################################################

#write a python program to add some days to your present date and print the date
import datetime
a=datetime.date.today()
b=datetime.timedelta(days=7)
print(a+b)
# Output:
# 2019-12-06

############################################

#write a python program to print the no. of days to write to reach your birthday
import datetime
a=datetime.date.today()
b=datetime.date(2020,5,27)
c=b-a
print(c)
###############################################
#write an python program to print date, time using date and time functions
import datetime
t=datetime.datetime.today()
print(t.date())
print(t.time())

##########################################
#write a python program to display time.
import time
print(time.time())
#########################################
#write a python program using sleep().
import time
time.sleep(6) #prints after 6 seconds
print("Python Lab")


#################################
#Calendar module:

#write a python program to display a particular month of a year using calendar
import calendar
print(calendar.month(2020,1))

#Output:
# write a python program to check whether the given y

################################################
# write a python program to check whether the given year is leap or not.
import calendar
print(calendar.isleap(2021))

######################################
#write a python program to print all the months of given year.
import calendar
print(calendar.calendar(2020,1,1,1))
#########################################
#math module:
# write a python program which accepts the radius of a circle from user and computes

import math
r=int(input("Enter radius:"))
area=math.pi*r*r
print("Area of circle is:",area)

#######################################################
#Import all names:
# We can import all names(definitions) from a module using the following construct.
#>>>from math import *
#>>>print("The value of pi is", pi