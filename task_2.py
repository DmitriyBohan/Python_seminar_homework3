""" 
Напишите программу, 
которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, 
второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15] 
"""

list = (2, 3, 4, 5, 6)


def mult_elements(arr):
    mult = 1
    for i in range(int((len(arr))/2)):
        mult = arr[i]*arr[-i-1]
        print(mult, end=' ')
    if (len(arr)) % 2 != 0:
        print(arr[int((len(arr))/2)]**2)


mult_elements(list)
