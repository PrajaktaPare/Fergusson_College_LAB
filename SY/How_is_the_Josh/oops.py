from abc import ABC, abstractmethod
class Account(ABC):
    acnt=0

    def __init__(self,acnt,anum,balance):
        self.acnt = acnt
        self.anum = anum
        self.balance = balance

    @abstractmethod
    def deposit(self , amount):
        pass

    @abstractmethod
    def withdraw(self , amount):
        pass    

    @abstractmethod
    def display_info(self):
        pass

class SavingsAccount(Account):
    def __init__(self, acnt, anum, balance):
        acnt=acnt+1
        self.anum=str(acnt)
        super().__init__(acnt, anum, balance)
       
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Amount.")
        else:
            self.balance -= amount
            print(f"Withdraw {amount}. New balance is {self.balance}")   

    def display_info(self):
        print(f"Account Number: {self.anum}, Balance: {self.balance}")

class CurrentAccount(Account):
    def __init__(self, acnt, anum, balance):
        acnt=acnt+1
        self.anum=str(acnt)
        super().__init__(acnt, anum, balance)
       
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Amount")
        else:
            self.balance -= amount
            print(f"Withdraw {amount} New balance is {self.balance}")   

    def display_info(self):
        print(f"Account Number: {self.anum}, Balance: {self.balance}")

while True:
    print("1. Create Savings Account")
    print("2. Create Current Account")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        