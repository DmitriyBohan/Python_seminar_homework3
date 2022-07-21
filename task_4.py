""" 
Напишите программу, 
которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10 
"""

number = int(input())
 
dec = ''
 
while number > 0:
    dec = str(number % 2) + dec
    number = number // 2
 
print(dec)