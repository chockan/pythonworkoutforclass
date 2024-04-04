import my


my.greeting("Jo")

a = my.person1["age"]
print(a)


#Create an alias for mymodule called mx:

import my as mx

a = mx.person1["age"]
print(a)


#import and use the platform module:

import platform

x = platform.system()
print(x)


x = dir(platform)
print(x)