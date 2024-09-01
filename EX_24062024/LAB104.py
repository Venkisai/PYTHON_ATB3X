N = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def even(num):
    return num % 2 == 0

def greater_5(num):
    return num > 5

NN = filter(even,N)
print(list(NN))

MN = filter(greater_5,N)
print(list(MN))
