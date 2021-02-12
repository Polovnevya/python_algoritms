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


def partition(array: list, left: int, right: int) -> int:
    pivot = array[(left + right) // 2]
    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    return right


def find_mid(data: list) -> list:
    pivot = len(data) // 2
    left = 0
    right = len(data) - 1
    while True:
        mid = partition(data, left, right)

        if mid == pivot:
            return data[mid]

        if pivot < mid:
            right = mid
        else:
            left = mid + 1


print(array)
print(find_mid(array))
