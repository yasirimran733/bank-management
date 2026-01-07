import json
import os
from operator import truediv

class AmountExecption(Exception):
    pass
class Account:
    accounts = []
    def __init__(self, cnic , name , balance):
        self.cnic = cnic
        self.name = name
        self.balance = balance
        f = open("accounts.json", 'w')
        print(f"{self.name} Your Account is created with balanace {self.balance}.")
        self.setBalance(f)

    def setBalance(self,f):
        accounts = []
        if os.path.getsize("accounts.json") != 0:
            with open("accounts.json", 'r') as f:
                accounts = json.load(f)
        account = {"cnic": self.cnic, "name": self.name, "balance": self.balance}
        accounts.append(account)
        json.dump(accounts, f)
    def checkBalance(self):
        if os.path.getsize("accounts.json") != 0:
            with open("accounts.json", 'r') as f:
                accounts = json.load(f)
                for account in accounts:
                    if account["cnic"] == self.cnic:
                        print(f"{self.name} Your current balance is {account["balance"]}")

    def deposit(self,amount):
        accounts = []
        with open("accounts.json", 'r') as f:
            accounts = json.load(f)
        for account in accounts:
            if account["cnic"] == self.cnic:
                account["balance"] = self.balance + amount
                self.balance = account["balance"]
                break
        with open("accounts.json", 'w') as f:
            json.dump(accounts, f)
            self.checkBalance()


    def withdraw(self,amount):
        try:
            if amount <= self.balance:
                self.balance = self.balance-amount
                self.getBalance()
            else:
                raise AmountExecption
        except AmountExecption:
            print(f"You cannot withdraw because you have just {self.balance} rupees .")

    def transfer(self,amount,toAccount):
        try:
            if amount<=self.balance:
                self.balance = self.balance - amount
                toAccount.deposit(amount)
                print(f"Amount is Transfered to {toAccount.name}.")
                self.checkBalance()
            else:
                raise AmountExecption
        except AmountExecption:
            print(f"You cannot transfer money because you have just {self.balance} rupees .")

# class SavingAccount(Account):
# class currentAccount(Account):
# class fixDepositAccount(Account):


class User:

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        with open("users.json","r") as f:
            users = json.load(f)
            for user in users:
                if user["username"] == username and user["password"] == password:
                    print(f"{username} logged in.")
                    return True
            print("Invalid username or password.Please try again.")
            return False

    def register(self):
        username = input("Enter your username: ")

        if os.path.getsize("users.json") != 0:
            with open("users.json", "r") as f:
                 users = json.load(f)
                 for user in users:
                     if user["username"] == username:
                        print(f"{username} Already registered.")
                        return False
        password = input("Enter your password: ")

        usersList = []

        if os.path.getsize("users.json") != 0:
            with open("users.json", "r") as f:
                 usersList = json.load(f)

        with open("users.json","w",encoding="utf-8") as f:
            user  = {"username":username,"password":password}
            usersList.append(user)
            json.dump(usersList,f)
            print(f"{username} registered successfully.")
            return True
#
#

Aftab  = Account(34101, "Aftab", 789)
Aftab.checkBalance()
Aftab.deposit(200)