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
# #print(b.a)
# b2=derived()
##############################################
# class Employee:
#     # constructor
#     def __init__(self, name, salary):
#         # public data member
#         self.name = name
#         # private member
#         self.__salary = salary
#         print('Salary:', self.__salary)

# # creating object of a class
# emp = Employee('Jessa', 10000)

# # accessing private data members
# # print('Salary:', emp.__salary)

###############################################

# class Company:
#     def __init__(self):
#         # Protected member
#         self._project = "NLP"

# child class
# class Employee(Company):
#     def __init__(self, name):
#         self.name = name
#         Company.__init__(self)

#     def show(self):
#         print("Employee name :", self.name)
#         # Accessing protected member in child class
#         print("Working on project :", self._project)

# c = Employee("Jessa")
# c.show()
# # Direct access protected data member
# print('Project:', c._project)

################################################

# class Employee:
#     # constructor
#     def __init__(self, name, salary):
#         # public data member
#         self.name = name
#         # private member
#         self.__salary = salary

# # creating object of a class
# emp = Employee('Jessa', 10000)

# print('Name:', emp.name)
# # direct access to private member using name mangling
# print('Salary:', emp._Employee__salary)
########################################################

# from abc import ABC, abstractmethod
# class democlass(ABC):
#    @abstractmethod
#    def method1(self):
#       print ("first method")

#    def method2(self):
#       print("metho2 ")

# class demo(democlass):
   
   
  
#    def method1(self):
#       print ("second method")
   

# a=demo()
# a.method1()
# a.method2()

####################################################
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
circle = Circle(6)
rectangle = Rectangle(5,7)
print(circle.area())  # Output: 113.09724
print(rectangle.area())  # Output: 35

del rectangle
#print(rectangle.area())

###################################################

from abc import ABC, abstractmethod
from random import randint

class Account(ABC):
    @abstractmethod
    def createAccount(self, name, initialDeposite):
        pass

    @abstractmethod
    def authenticate(self, name, accountNumber):
        pass

    @abstractmethod
    def withdraw(self, withdrawAmount):
        pass

    @abstractmethod
    def deposit(self, depositAmount):
        pass

    @abstractmethod
    def displaybalance(self):
        pass

class SavingAccount(Account):
    def __init__(self):
        self.savingAccounts = {"11111": ["hemil", 1]}
        self.accountNumber = None

    def createAccount(self, name, initialDeposite):
        self.accountNumber = str(randint(10000, 99999))
        self.savingAccounts[self.accountNumber] = [name, initialDeposite]
        print("Your account is successfully created, Your account number is {}".format(self.accountNumber))

    def authenticate(self, name, accountNumber):
        if accountNumber in self.savingAccounts.keys():
            if self.savingAccounts[accountNumber][0] == name:
                print("Authentication Successful!")
                self.accountNumber = accountNumber
                return True
        print("Authentication failed")
        return False

    def withdraw(self, withdrawAmount):
        if self.accountNumber is None:
            print("Please authenticate first.")
            return

        if withdrawAmount > self.savingAccounts[self.accountNumber][1]:
            print("Insufficient Balance")
        else:
            self.savingAccounts[self.accountNumber][1] -= withdrawAmount
            print("Withdraw Successful")
            self.displaybalance()

    def deposit(self, depositAmount):
        if self.accountNumber is None:
            print("Please authenticate first.")
            return

        self.savingAccounts[self.accountNumber][1] += depositAmount
        print("Deposit Successful")
        self.displaybalance()

    def displaybalance(self):
        if self.accountNumber is None:
            print("Please authenticate first.")
            return

        print("Available balance: {}".format(self.savingAccounts[self.accountNumber][1]))


savingAccount = SavingAccount()

while True:
    print("Enter 1 to open an account")
    print("Enter 2 to access an existing account")
    print("Enter 3 to exit")
    userChoice = int(input(""))
    if userChoice == 1:
        name = input("Enter your name: ")
        initialDeposit = int(input("Enter initial deposit: "))
        savingAccount.createAccount(name, initialDeposit)

    elif userChoice == 2:
        name = input("Enter name: ")
        accountNumber = input("Enter account number: ")
        authenticateStatus = savingAccount.authenticate(name, accountNumber)
        if authenticateStatus:
            while True:
                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to display balance")
                print("Enter 4 to exit")
                userChoice = int(input(""))
                if userChoice == 1:
                    withdrawAmount = int(input("Enter withdraw amount: "))
                    savingAccount.withdraw(withdrawAmount)
                elif userChoice == 2:
                    depositAmount = int(input("Enter deposit amount: "))
                    savingAccount.deposit(depositAmount)
                elif userChoice == 3:
                    savingAccount.displaybalance()
                elif userChoice == 4:
                    break

    elif userChoice == 3:
        break
