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
run('func_1(100_000)')
"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.177    0.177 <string>:1(<module>)
   100000    0.057    0.000    0.126    0.000 random.py:174(randrange)
   100000    0.025    0.000    0.150    0.000 random.py:218(randint)
   100000    0.048    0.000    0.068    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.176    0.176 task_1.py:12(func_1)
        1    0.019    0.019    0.169    0.169 task_1.py:15(<listcomp>)
        1    0.008    0.008    0.008    0.008 task_1.py:16(<listcomp>)
        1    0.000    0.000    0.177    0.177 {built-in method builtins.exec}
   100000    0.006    0.000    0.006    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   126960    0.014    0.000    0.014    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
print('********************************************************************')
print(timeit('ugly_func(1_00)', number=100, globals=globals()))  # 0.01381810000000172
print(timeit('ugly_func(1_000)', number=100, globals=globals()))  # 0.14056080000000115
print(timeit('ugly_func(10_000)', number=100, globals=globals()))  # 2.0527015000000013
print(timeit('ugly_func(100_000)', number=100, globals=globals()))  # 123.46583239999998
run('ugly_func(100_000)')
"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    1.363    1.363 <string>:1(<module>)
   100000    0.058    0.000    0.127    0.000 random.py:174(randrange)
   100000    0.024    0.000    0.152    0.000 random.py:218(randint)
   100000    0.048    0.000    0.069    0.000 random.py:224(_randbelow)
        1    0.031    0.031    1.362    1.362 task_1.py:20(ugly_func)
        1    0.069    0.069    1.173    1.173 task_1.py:25(_get_even_indexes)
        1    0.000    0.000    1.363    1.363 {built-in method builtins.exec}
   150481    0.011    0.000    0.011    0.000 {method 'append' of 'list' objects}
   100000    0.007    0.000    0.007    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   126359    0.014    0.000    0.014    0.000 {method 'getrandbits' of '_random.Random' objects}
   100000    0.014    0.000    0.014    0.000 {method 'index' of 'list' objects}
   100000    1.086    0.000    1.086    0.000 {method 'pop' of 'list' objects}
"""
print('********************************************************************')
print(timeit('func_3(1_00)', number=100, globals=globals()))  # 0.011017199999997729
print(timeit('func_3(1_000)', number=100, globals=globals()))  # 0.12025529999999662
print(timeit('func_3(10_000)', number=100, globals=globals()))  # 1 .1227595000000008
print(timeit('func_3(100_000)', number=100, globals=globals()))  # 11.986708399999998
run('func_3(100_000)')
"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.203    0.203 <string>:1(<module>)
   100000    0.064    0.000    0.139    0.000 random.py:174(randrange)
   100000    0.026    0.000    0.165    0.000 random.py:218(randint)
   100000    0.053    0.000    0.075    0.000 random.py:224(_randbelow)
        1    0.016    0.016    0.203    0.203 task_1.py:47(func_3)
        1    0.020    0.020    0.184    0.184 task_1.py:51(<listcomp>)
        1    0.000    0.000    0.203    0.203 {built-in method builtins.exec}
    50755    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
   100000    0.006    0.000    0.006    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   126748    0.015    0.000    0.015    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
"""
Варианты 1, 3 имеют поти равно время и зависимость похожа на линейную
Вариант 2 имеет квадратичную зависимость, с увеличением параметра сложность очень сильно вырастает.
 Судя по cProfile метод списков .pop очень сильно усложняет алгоритм
"""
