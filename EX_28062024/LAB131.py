class BankAccount:
    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_func(self):
        print(self.__private_var)

    def deposit(self, balance):
        self.balance += balance

    def __withdraw(self, balance):
        self.balance -= balance

    def __show_balance(self):
        print("Your balance is", self.balance)

    def if_you_are_auth(self, flag):
        if flag:
            self.__show_balance()
        else:
            print("Not Allowed")

    def if_you_are_auth_user(self, auth, balance):
        if auth:
            self.__withdraw(balance = balance)
        else:
            ("You can't withdraw")


SBI = BankAccount()
SBI.deposit(1000)

secret_pass = input("Enter your PIN to see your balance")
if secret_pass == "3456":
    SBI.if_you_are_auth(True)
else:
    SBI.if_you_are_auth(False)

secret_pass = input("Enter your PIN to withdraw")
your_amount = int(input("Enter the amount you want to withdraw"))
if secret_pass == "3456":
    SBI.if_you_are_auth_user(True, balance =your_amount )
    SBI.if_you_are_auth(True)
else:
    SBI.if_you_are_auth(False)

