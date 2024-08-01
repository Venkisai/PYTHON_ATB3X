#Inbuilt functions
#To repeat a task - we can use a function
#Functions are print(), max(), min(), id(),input(), type(), format(), sum(), avg()
name = "Yejas"
print(name)
print(type(name))
print(id(name))
print(len(name))
name = name.upper()
print(name)
name = name.lower()
print(name)
name = name.casefold()
print(name)
name = name.capitalize()
print(name)
b = name.count('a')
print(b)
print(name[4])
#In python strings are immutable-cannot change the value
name[0] = "V"
#The above line shows Type Error: 'str' object does not support item assignment