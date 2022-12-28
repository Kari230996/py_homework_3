# 1) Задайте список из нескольких чисел. Напишите программу,
#    которая найдёт сумму элементов списка, стоящих на нечётной позиции.


import random

N = 10
array = [random.randint(1, 20) for i in range(N)]
length = len(array)
print(array)

arr = []

for i in range(length):
    if i % 2 != 0:
        arr.append(array[i])
print(arr)

print(f"На нечётных позициях элементы {arr}, ответ: {sum(arr)}")