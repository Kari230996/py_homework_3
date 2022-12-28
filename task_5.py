# 5) Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

'''
fib1 = fib2 = 1

num = int(input('Choose a number: '))

print(fib1, fib2, end=' ')

for i in range(2, num):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')

'''


def positive_fib(k):
    fib_list = [1, 1]
    for i in range(k-2):
        fib_list.append(fib_list[-2] + fib_list[-1])

    return fib_list


def negative_fib(k):
    fib_list = [0, 1]
    for i in range(k-1):
        fib_list.append(fib_list[-2] - fib_list[-1])
    return fib_list[::-1]

print(negative_fib(8)+positive_fib(8))