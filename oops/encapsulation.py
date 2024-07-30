# This put restrictions on access variables and methods directly and can prevent the accidental modification of data.

# class base:
#     def __init__(self):
#         self.a=20
#     def ddd(self):
#         print("from base :",self.a)
# class derived(base):
#     def __init__(self):
#         super().__init__()
#         print("from derived:",self.a)

# b=base()
# b.ddd()
# print(b.a)
# b2=derived()
###########################################

#private variables
#only acccess within the class
# class base:
#     def __init__(self):
#         self.__a=20
#     def ddd(self):
#         print("from base :",self.__a)
# class derived(base):
#     def __init__(self):
#         super().__init__()
#         print("from derived:",self.__a)

# b=base()
# b.ddd()
#print(b.a)
# b2=derived()

##########################################

class base:
    def __init__(self):
        self.a=20
    def __ddd(self):
        print("from base :",self.a)
class derived(base):
    def __init__(self):
        super().__init__()
        print("from derived:",self.a)

b=base()
b.__ddd()
#print(b.a)
b2=derived()
# ########################################################
# class Employee:
#     # constructor
#     def __init__(self, name, salary):
#         # public data member
#         self.name = name
#         # private member
#         self.__salary = salary

# # creating object of a class
# emp = Employee('Jessa', 10000)

# # accessing private data members
# print('Salary:', emp.__salary)

# #########################################################
# class Employee:
#     # constructor
#     def __init__(self, name, salary):
#         # public data member
#         self.name = name
#         # private member
#         self.__salary = salary

#     # public instance methods
#     def show(self):
#         # private members are accessible from a class
#         print("Name: ", self.name, 'Salary:', self.__salary)

# # creating object of a class
# emp = Employee('Jessa', 10000)

# # calling public method of the class
# emp.show()

############################################################
class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

# creating object of a class
emp = Employee('Jessa', 10000)

print('Name:', emp.name)
# direct access to private member using name mangling
print('Salary:', emp._Employee__salary)
#################################################################
# base class
class Company:
    def __init__(self):
        # Protected member
        self._project = "NLP"

# child class
class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)

    def show(self):
        print("Employee name :", self.name)
        # Accessing protected member in child class
        print("Working on project :", self._project)

c = Employee("Jessa")
c.show()


# Direct access protected data member
print('Project:', c._project)
#########################################################