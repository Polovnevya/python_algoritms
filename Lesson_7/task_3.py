"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану.
Медианой называется элемент ряда,
 делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

"""

from random import randint
from timeit import timeit

START = -100
STOP = 100
M = 5
SIZE = 2 * M + 1
array = [randint(START, STOP) for i in range(SIZE)]


def my_sort(data: list) -> list:
    array = data.copy()
    num = len(array) // 2
    return array


a = my_sort(array)
