#To calculate the area of a circle
#The formula is pi*r*r
#We need a radius value
#for the value of pi we have to import
import math
r = input("Enter the radius:\n")
r = float(r)
print(math.pi)
area = math.pi*(r**2)
area2 = math.pi*(math.pow(r,2))
print(area)
print(area2)

