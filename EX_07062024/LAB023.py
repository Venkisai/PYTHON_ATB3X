#List - A group of elements
#milk, butter, poha, oil
#In list we can add an item
#we can remove an item
#we can Update an item
#we can view an item
A = ['milk', 'bread', 'butter', 'poha' ]
print(A)
print(len(A))
print(A[0])
print(A[-1])
A.append("curd")
print(A)
A.insert(1,"jam")
print(A)
A.extend(["salt", "chips"])
print(A)
A.insert(3, "oil")
print(A)
print(len(A))
A.remove("bread")
print(A)
print(A.pop())
print(A.index("butter"))
A.reverse()
print(A)
A.sort()
print(A)
A[0] = "Venkat"
print(A)



B = [1, 'Venkat', 77.78, True, "Distinction", 10+20j]
print(B)
print(len(B))
print(B[0])
print(type(B[0]))
print(B[1])
print(type(B[1]))
print(len(B[1]))
print(id(B[1]))
print(B[2])
print(type(B[2]))
print(id(B[2]))
print(B[3])
print(type(B[3]))
print(id(B[3]))
print(B[4])
print(type(B[4]))
print(len(B[4]))
print(id(B[4]))
print(B[5])
print(type(B[5]))
print(id(B[5]))