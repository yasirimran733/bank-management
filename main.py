class AmountExecption(Exception):
    pass

class Account:
    def __init__(self,name , balance):
        self.name = name
        self.balance = balance
        print(f"{self.name} you Account is created with balanace {self.balance}.")

    def getBalance(self):
        print(f"{self.name} Your current balance is {self.balance}")

    def deposit(self,amount):
        self.balance=self.balance+amount
        self.getBalance()

    def withdraw(self,amount):
        try:
            if amount <= self.balance:
                self.balance = self.balance-amount
                self.getBalance()
            else:
                raise AmountExecption
        except AmountExecption:
            print(f"You cannot withdraw because you have just {self.balance} rupees .")




acc = Account("Yasir",100)
acc.deposit(120)
acc.deposit(23)
acc.withdraw(243)
