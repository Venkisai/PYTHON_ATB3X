numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def double(i):
    return i * 2

after_double = map(double, numbers)
print(list(after_double))


def even(i):
    return i % 2 == 0

only_even = filter(even, numbers)
print(list(only_even))