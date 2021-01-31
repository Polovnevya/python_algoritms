"""
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
    второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
    т.к. именно в этих позициях первого массива стоят четные числа.
"""

from random import randint


def func_1() -> list:
    MIN_ITEM = 0
    MAX_ITEM = 100
    SIZE = 10
    array = [randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
    second_array = [index for index, val in enumerate(array) if val % 2 == 0]
    return second_array


def ugly_func() -> list:
    MIN_ITEM = 0
    MAX_ITEM = 100
    START = 0
    END = 10
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

    for i in range(START, END):
        array.append(randint(MIN_ITEM, MAX_ITEM))

    return _get_even_indexes(array)


def func_3():
    MIN_ITEM = 0
    MAX_ITEM = 100
    SIZE = 10
    even_indexes_array = []
    array = [randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
    for i, el in enumerate(array):
        if el % 2 == 0:
            even_indexes_array.append(i)
    return even_indexes_array

a = ugly_func()
a = func_3()

v = 1
