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


def func_2() -> list:
    MIN_ITEM = 0
    MAX_ITEM = 100
    START = 0
    END = 10
    array = []

    for i in range(START, END):
        array.append(randint(MIN_ITEM, MAX_ITEM))

    def _get_even_indexes(user_list: list) -> list:
        even_indexes_array = []
        for el in user_list:
            if el % 2 == 0:
                ind = user_list.index(el)
                even_indexes_array.append(ind)
                el = user_list.pop(ind)
        v=1
        return _get_even_indexes(array)

a = func_2()
