"""
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
    второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
    т.к. именно в этих позициях первого массива стоят четные числа.
"""
from timeit import timeit
from cProfile import run
from random import randint


def func_1(size: int) -> list:
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [randint(MIN_ITEM, MAX_ITEM) for i in range(size)]
    second_array = [index for index, val in enumerate(array) if val % 2 == 0]
    return second_array


def ugly_func(size: int) -> list:
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = []

    def _get_even_indexes(user_list: list) -> list:
        array = user_list.copy()
        even_indexes_array = []
        i = 0
        while array:
            el = array[0]
            if el % 2 == 0:
                ind = array.index(el)
                even_indexes_array.append(i)
                array.pop(ind)
            else:
                ind = array.index(el)
                array.pop(ind)
            i += 1
        return even_indexes_array

    for i in range(size):
        array.append(randint(MIN_ITEM, MAX_ITEM))

    return _get_even_indexes(array)


def func_3(size: int) -> list:
    MIN_ITEM = 0
    MAX_ITEM = 100
    even_indexes_array = []
    array = [randint(MIN_ITEM, MAX_ITEM) for i in range(size)]
    for i, el in enumerate(array):
        if el % 2 == 0:
            even_indexes_array.append(i)
    return even_indexes_array


print(timeit('func_1(1_00)', number=100, globals=globals()))  # 0.011403700000000003
print(timeit('func_1(1_000)', number=100, globals=globals()))  # 0.1505243
print(timeit('func_1(10_000)', number=100, globals=globals()))  # 1.1570426999999999
print(timeit('func_1(100_000)', number=100, globals=globals()))  # 11.6363716
print('********************************************************************')
print(timeit('ugly_func(1_00)', number=100, globals=globals()))  # 0.01381810000000172
print(timeit('ugly_func(1_000)', number=100, globals=globals()))  # 0.14056080000000115
print(timeit('ugly_func(10_000)', number=100, globals=globals()))  # 2.0527015000000013
print(timeit('ugly_func(100_000)', number=100, globals=globals()))  # 123.46583239999998
print('********************************************************************')
print(timeit('func_3(1_00)', number=100, globals=globals()))  # 0.011017199999997729
print(timeit('func_3(1_000)', number=100, globals=globals()))  # 0.12025529999999662
print(timeit('func_3(10_000)', number=100, globals=globals()))  # 1 .1227595000000008
print(timeit('func_3(100_000)', number=100, globals=globals()))  # 11.986708399999998
