# 4) Напишите программу, которая будет преобразовывать десятичное число в двоичное.

n = int(input('Choose a number: '))

binary = ''

while n > 0:
    binary = str(n % 2) + binary
    n = n // 2

print(binary)