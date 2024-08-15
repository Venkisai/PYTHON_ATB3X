class BankAccount:
    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_func(self):
        print(self.__private_var)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print("Your balance is", self.balance)


SBI = BankAccount()
print(SBI.balance)
SBI.deposit(101)
SBI.show_balance()
SBI.deposit(99)
SBI.show_balance()
SBI.withdraw(199)
SBI.show_balance()