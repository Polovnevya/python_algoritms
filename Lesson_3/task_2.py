"""
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
    второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
    т.к. именно в этих позициях первого массива стоят четные числа.
"""

from random import randint

MIN_ITEM = 0
MAX_ITEM = 100
SIZE = 10
array = [randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(f'Исходный массив {array}')
second_array = [index for index, val in enumerate(array) if val % 2 == 0]
print(f'Массив с индексами четных чисел {second_array}')
