print("---Starting of the program---")
try:
    a = int(input("\nEnter number1: "))
    b = int(input("\nEnter number2: "))
    c = a / b
    print("Result is", c)
except Exception as e:
    print(e)
    print("Please enter an integer")


print("---Ending of the program---")