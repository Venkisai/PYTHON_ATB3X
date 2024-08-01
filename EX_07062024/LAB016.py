#add two integer numbers to find sum of them
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
result = num1 + num2
print(result)
#so we need here a type conversion i.e, 'str' to 'int'
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
result = int(num1) + int(num2)
print(result)
#here '+' acts as 2 types
#in case of adding 2 strings it acts as 'concatination'
#in case of adding 2 integers it acts as 'sum'
print(type(int(num1)))
print(type(int(num2)))