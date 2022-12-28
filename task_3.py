# 3) Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
#    минимальным значением дробной части элементов.

import random
N = 10
array = [round(random.uniform(0, 10), 2) for i in range(1, N+1)]

print(array)

maxi = array[0]
mini = array[0]

for i in array:

    if i > maxi:
        maxi = i

for i in array:
    if i < mini:
        mini = i

print(f'Разность между макс. {maxi} и мин. {mini} числами: {maxi - mini}')
