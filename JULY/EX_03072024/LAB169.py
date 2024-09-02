import os
cwd = os.getcwd()#C:\VENKATESH\PYTHON ATB3X\JULY\EX_03072024

print(os.getcwd())
file = open("TestData2.txt", 'r')
content = file.read()
print(content)
file.close()