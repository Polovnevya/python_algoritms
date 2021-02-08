"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
версия Python

Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
 Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)]
версия ОС Win10 x64
"""

import sys
from collections import deque, Counter


def show_mem(obj):
    print(f'{type(obj)}\t{sys.getsizeof(obj)}\t{obj}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items:
                show_mem(key)
                show_mem(value)
        elif not isinstance(obj, str):
            for item in obj:
                show_mem(item)


def func_var_list(start: int, end: int):
    for i in range(2, 10):
        array = [el for el in range(start, end, i) if el >= i and el <= end]
        show_mem(array)
        print(f'В диапазоне {start} - {end} находится {len(array)} чисел кратных {i}')
    show_mem(i)
    show_mem(start)
    show_mem(end)
    return None


def func_var_tuple(start: int, end: int):
    for i in range(2, 10):
        array = tuple([el for el in range(start, end, i) if el >= i and el <= end])
        show_mem(array)
        print(f'В диапазоне {start} - {end} находится {len(array)} чисел кратных {i}')
    show_mem(i)
    show_mem(start)
    show_mem(end)
    return None


def func_var_set(start: int, end: int):
    for i in range(2, 10):
        array = set([el for el in range(start, end, i) if el >= i and el <= end])
        show_mem(array)
        print(f'В диапазоне {start} - {end} находится {len(array)} чисел кратных {i}')
    show_mem(i)
    show_mem(start)
    show_mem(end)
    return None


def func_var_deque(start: int, end: int):
    for i in range(2, 10):
        array = deque([el for el in range(start, end, i) if el >= i and el <= end])
        show_mem(array)
        print(f'В диапазоне {start} - {end} находится {len(array)} чисел кратных {i}')
    show_mem(i)
    show_mem(start)
    show_mem(end)
    return None


def func_var_1(start: int, end: int):
    array_1 = [i for i in range(2, 10)]
    array_2 = [i for i in range(start, end)]
    array_3 = []
    for ham in array_1:
        for spam in array_2:
            if spam >= ham and spam <= end and spam % ham == 0:
                array_3.append(spam)
        show_mem(array_3)
        show_mem(array_2)
        show_mem(array_1)
        print(f'В диапазоне {start} - {end} находится {len(array_3)} чисел кратных {ham}')
    return None



func_var_list(0, 100)
func_var_tuple(0, 100)
func_var_set(0, 100)
func_var_deque(0, 100)
func_var_1(0, 100)
