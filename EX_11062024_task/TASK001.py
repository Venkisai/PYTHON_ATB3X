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


#[33, 12, 16, 4, 5]
l = [33, 12, 16, 4, 5]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            #swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubble_sort(l)
print("sorted list", l)



my_list = [22, 44, 12, 3, 67]
largest = my_list[0]
for number in my_list:
    if number > largest:
        largest = number


print("The largest number in the list is", largest)


list1 = [22, 44, 12, 3, 67]
largest = max(list1)
print("The largest number in the list is", largest)
print(largest)

