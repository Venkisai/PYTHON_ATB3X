#Difference between '=' and '==' operators
#Here '=' operator is used as assignment i.e,
x = 10
y = 10
if x > y :
    print("x is greater")
elif x < y :
    print("y is greater")
else:
    print("both are equal")
#here '=' is assigned value '10' to the x and y


a = 1000
b = 1000
if a == b:
    print("it is true")
else:
    print("it is false")
print(id(a))
print(id(b))
#here a and b value is assigned to the same address but for different objects
#finally '=' is assignment operator and '==' is comparison operator or relational operator