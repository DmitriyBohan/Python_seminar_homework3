""" 
Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу между максимальным 
и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19 
"""

list = (1.1, 1.2, 3.1, 5, 10.01)


def min_max_find(arr):
    min = arr[0] - int(arr[0])
    max = arr[0] - int(arr[0])
    res = 0
    for i in range(len(arr)):
        if arr[i]-int(arr[i]) < min:
            min = arr[i]-int(arr[i])
        if arr[i]-int(arr[i]) > max:
            max = arr[i]-int(arr[i])
    res = max-min
    return res


print((str(min_max_find(list)))[0:4])
