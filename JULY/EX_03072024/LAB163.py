class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message + "Custom Message"
        super().__init__(message)


balance = 100
withdraw = int(input("Enter the amount"))
if withdraw > balance:
    raise MyCustomException("Balance is low!!")
else:
    print("Remain Balance", (balance - withdraw))