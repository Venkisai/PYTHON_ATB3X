#what is '**" operator? Why do we use this?
p = 4
q = 5
print(p*q)
#the above statement shows us product of 2 objects


a = 7
b = 4
result = a*b
print(result)
#we can use both the programs for product of 2 objects


#if we use 2 ** at a time it shows the exponent of two objects
#and it is called as exponential operator
#Let us see
x = 9
y = 6
result1 = x**y
print(result1)


x1 = 6
y1 = 3
print(x1**y1)


import math
x2 = 5
y2 = 2
print(math.pow(x2, y2))


A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
print(A**B)
print(math.pow(A, B))