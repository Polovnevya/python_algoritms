"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

import sys


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


def func_var_1(start: int, end: int):
    for i in range(2, 10):
        array = [el for el in range(start, end, i) if el >= i and el <= end]
        show_mem(array)
        print(array)
        print(f'В диапазоне {start} - {end} находится {len(array)} чисел кратных {i}')
    return None


def func_var_2(start: int, end: int):
    array = ()
    for i in range(2, 10):
        array = tuple([el for el in range(start, end, i) if el >= i and el <= end])
        print(array)
        print(f'В диапазоне {start} - {end} находится {len(array)} чисел кратных {i}')

    return None


func_var_1(0, 10)
func_var_2(0, 10)
