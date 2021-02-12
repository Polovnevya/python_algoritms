"""
1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
 заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
 Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""

from random import randint
from timeit import timeit


def bubble_sort(data: list) -> list:
    array = data.copy()
    n = 1
    while n < len(array):
        for i in range(0, len(array) - 1):
            if array[i] > array[i + 1]:
                array[i + 1], array[i] = array[i], array[i + 1]
        n += 1
    return array


def bubble_sort_v2(data: list) -> list:
    array = data.copy()
    n = 1
    while n < len(array):
        for i in range(0, len(array) - n):
            if array[i] > array[i + 1]:
                array[i + 1], array[i] = array[i], array[i + 1]
        n += 1
    return array


START = -100
STOP = 100
SIZE = 1000
array = [randint(START, STOP) for i in range(SIZE)]

print(f'Исходный массив')
# print(array)

print(f'Сортировка пузырьком')
print(timeit('bubble_sort(array)', number=100, globals=globals()))  # 13.645704700000001
# print(bubble_sort(array))

print(f'Сортировка пузырьком v2')
print(timeit('bubble_sort_v2(array)', number=100, globals=globals()))  # 8.627556299999998
# print(bubble_sort_v2(array))
