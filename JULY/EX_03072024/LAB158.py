try:
    num1 = int(input("Enter first number: \n"))
    num2 = int(input("Enter second number: \n"))
    result = num1/num2
    print(result)
except Exception as e:
    print(e)


try:
    numa = int(input("Enter number a: \n"))
    numb = int(input("Enter number b: \n"))
    result = numa/numb
    print(result)
except ValueError as e1:
    print(e1)
except ZeroDivisionError as e2:
    print(e2)
else:
    print(f'Result is {result}')
finally:
    print("Anyhow I will execute")