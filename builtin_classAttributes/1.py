"""
The built-in class attributes provide us with information about the class.

Using the dot (.) operator, we may access the built-in class attributes.

The built-in class attributes in python are listed below −

Attributes	Description
__dict__==============Dictionary containing the class namespace
__doc__	============If there is a class documentation class, this returns it. Otherwise, None
__name__=============	Class name.
__module__ =========Module name in which the class is defined. This attribute is "__main__" in interactive mode.
__bases__ =========A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.

"""

# creating a class say 
# class abc:
#    'Welcome to abc Python'

#    def __init__(self):
#       print("The __init__ method")

# # Printing the value of Built-in __dict__ attribute for the abc class
# print(abc.__dict__)

####################################################
# # creating a class say 
# class abc:
#    'Welcome to abc Python'

#    def __init__(self):
#       print("The __init__ method")

# # getting the documentation for the  using
# # built-in __doc__ class attribute
# print(abc.__doc__)

##############################################

# class abc:
#    'Welcome to abc Python'

#    def __init__(self):
#       print("The __init__ method")

# # getting the name of the class using built-in __name__ class attribute
# print(abc.__name__)

#####################################################
# class abc:
#    'Welcome to abc Python'

#    def __init__(self):
#       print("The __init__ method")

# # getting the module of the class using built-in __module__ class attribute
# print(abc.__module__ )


########################################################

class abc:
   'Welcome to abc Python'

   def __init__(self):
      print("The __init__ method")

# getting the bases of the class using built-in __bases__ class attribute
print(abc.__bases__)

############################################################

# Creating a parent class with the name Employee
# class Employee:
#    'Common base class for all employees'
#    # initiaizing the variable with 0 for storing the employ count
#    empCount = 0

#    # init constructor which accepts the name, salary as arguments
#    def __init__(self, name, salary):

#       # Initialize the values of instance attributes
#       self.name = name
#       self.salary = salary

#       # incrementing the employ count by 1
#       Employee.empCount += 1

#    # displayCount () which prints the total employ count
#    def displayCount(self):
#       print("Total Employee :",Employee.empCount)

#    # creating another function i.e, displayEmployee
#    def displayEmployee(self):
#       print ("Name : ", self.name, ", Salary: ", self.salary)

# # creating child class with the name subEmployee inheriting properties
# # from the parent Employee class
# class subEmployee(Employee):
#    'Derived class for Base - Employee Class'

# # printing Employee class with documentation using __doc__ class attribute
# print( Employee.__doc__)

# # printing the name of the Employee class using __name__ class attribute
# print(Employee.__name__)

# # printing the module of the Employee class using __module__ class attribute
# print(Employee.__module__)

# # printing the dictionary containing the Employee class namespace
# # using __dict__ class attribute
# print(Employee.__dict__)

# # printing all the base classes for the derived class using __bases__ class attribute
# print(subEmployee.__bases__)