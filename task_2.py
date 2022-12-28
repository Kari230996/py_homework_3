# 2) Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
#    второй и предпоследний и т.д.

from random import randint

N = 10

array = [randint(1, 20) for i in range(1, N+1)]


print(array)

left = array[0:(len(array) // 2)]
right = array[(len(array) // 2)::]

print(left)
print(right)


new = [a*b for a, b in zip(left, right)]

if len(left) == len(right):
    print(new)

else:
    print('error')
