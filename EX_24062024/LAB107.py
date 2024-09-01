numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def doubler(number):
    return number * 2


def even(number):
    return number % 2 == 0


numbers_even = filter(even, numbers)
after_double = map(doubler, numbers)


print(list(numbers_even))
print(list(after_double))
