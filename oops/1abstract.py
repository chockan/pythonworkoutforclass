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
