"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
 заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.

"""
from random import randint
from timeit import timeit

START = 0
STOP = 49
SIZE = 1000
array = [randint(START, STOP) for i in range(SIZE)]


def merge_arrays(array_1: list, array_2: list) -> list:
    tmp_array = []
    if len(array_1) < len(array_2):
        array_1, array_2 = array_2, array_1

    array_1_idx = 0
    array_2_idx = 0
    for i in range(len(array_1) + len(array_2)):
        if array_2_idx < len(array_2) and array_1_idx < len(array_1):
            if array_1[array_1_idx] <= array_2[array_2_idx]:
                tmp_array.append(array_1[array_1_idx])
                array_1_idx += 1
            elif array_2[array_2_idx] < array_1[array_1_idx]:
                tmp_array.append(array_2[array_2_idx])
                array_2_idx += 1
        elif array_2_idx < len(array_2):
            tmp_array.append(array_2[array_2_idx])
            array_2_idx += 1
        elif array_1_idx < len(array_1):
            tmp_array.append(array_1[array_1_idx])
            array_1_idx += 1
    return tmp_array


def merge_sort(data: list) -> list:
    if len(data) == 1:
        return data
    else:
        mid = len(data) // 2
        first_array = merge_sort(data[:mid])
        second_array = merge_sort(data[mid:])
        return merge_arrays(first_array, second_array)


print(f'Исходный массив {array}')
print(f'Массив после сортировки {merge_sort(array)}')
print(timeit('merge_sort(array)', number=100, globals=globals()))  # 0.44002020000000003
