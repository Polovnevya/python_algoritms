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
            # без () нехотела работать obj.items() с Counter, в чем подвох?
            for key, value in obj.items():
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
    for ham in array_1:
        array_3 = []
        for spam in array_2:
            if spam >= ham and spam <= end and spam % ham == 0:
                array_3.append(spam)
        show_mem(array_3)
        print(f'В диапазоне {start} - {end} находится {len(array_3)} чисел кратных {ham}')

    show_mem(array_2)
    show_mem(array_1)
    return None


def func_var_2(start: int, end: int):
    def check(divider: int, digit: int, end: int) -> bool:
        if digit >= divider and digit <= end and digit % divider == 0:
            return True
        else:
            return False

    for i in range(2, 10):
        array = Counter([check(i, x, end) for x in range(start, end, i)])
        show_mem(array)
        print(f'В диапазоне {start} - {end} находится {array[True]} чисел кратных {i}')


func_var_list(0, 100)
func_var_tuple(0, 100)
func_var_set(0, 100)
func_var_deque(0, 100)
func_var_1(0, 100)
func_var_2(0, 100)

"""
Вывод:
в текущих задачах размер занимаемой памяти зависит от типа применяемых коллекций, количества коллекций
 и размера коллекций
 для функций указан максимальный размер занимаемой памяти, хранение 49 элементов + 4 переменых el, i, END = 28 байт,
 START = 0 и занимает в памяти 24 байта
 на каждой итерации высчитывается коллекция которая потом выводится на печать
размер занимаемой памяти 1 элемента везде одинаков и равен 28 байт, как и количество элементов,
 разница заключается в типе коллекции
 *******************************************************************************************************************
func_var_list(0, 100)  = ((49+3) * 28) + 528 + 24    = 2008
func_var_tuple(0, 100) = ((49+3) * 28) + 440 + 24    = 1920  
func_var_set(0, 100)   = ((49+3) * 28) + 2272 + 24   = 3752
func_var_deque(0, 100) = ((49+3) * 28) + 632 + 24    = 2112
func_var_1(0, 100) = ((49+3) * 28) + 528 + 24 + 352 + 3708 = 6068 см строка 157.
func_var_2(0, 100) = 24(bool->false) + 28(int) + 28(bool->true)  + 28(int) + 256 (счетчик Counter) + (28 * 3) + 24
 = 500 ***********самый оптимальный вариант см строка 167*************

по таблице видно что после увеличения количества элементов с 16 до 19 происходит резкий рост резервируемой памяти для
коллекций список (list) и множеств (set)

в то же время коллекция очередь (deque) имеет изначально большой размер и на приведенной выборке данных
    размер резервируемой памяти под данную коллекцию не меняется
    
на малых значениях, до 19 элементов list не сильно уступает кортежу (tuple), но tuple вне конкуренции

*******************************************************************************************************************
<class 'list'>	528	<class 'tuple'>	440	<class 'set'>	2272	<class 'collections.deque'>	632
49 элементов кратных 2
<class 'list'>	344	<class 'tuple'>	312	<class 'set'>	2272	<class 'collections.deque'>	632
33 элементов кратных 3
<class 'list'>	264	<class 'tuple'>	240	<class 'set'>	2272	<class 'collections.deque'>	632
24 элементов кратных 4
<class 'list'>	264	<class 'tuple'>	200	<class 'set'>	2272	<class 'collections.deque'>	632
19 элементов кратных 5

*******************************************************************************************************************

<class 'list'>	192	<class 'tuple'>	176	<class 'set'>	736	<class 'collections.deque'>	632
16 элементов кратных 6
<class 'list'>	192	<class 'tuple'>	160	<class 'set'>	736	<class 'collections.deque'>	632
14 элементов кратных 7
<class 'list'>	192	<class 'tuple'>	144	<class 'set'>	736	<class 'collections.deque'>	632
12 элементов кратных 8
<class 'list'>	192	<class 'tuple'>	136	<class 'set'>	736	<class 'collections.deque'>	632
11 элементов кратных 9
*******************************************************************************************************************

Функция func_var_1 выполнена другим алгоритмом, имеет 2 дополнительных списка,
    которые живут все действие программы, списки испольуются как константы и не изменяются в процессе работы.
    целесообразно заменить их на tuple
    array_1= 8(количестко элементов)  * 28(размер элемента) + 128(размер списка) = 352
    array_2= 99(количестко элементов) * 28(размер элемента) + 24(ноль) + 912(размер списка) = 3708

func_var_1(0, 100) = ((49+3) * 28) + 528 + 24 + 352 + 3708 = 6068
самый плохой вариант

*******************************************************************************************************************
Оптимизированный вариант алгоритма, производится приведение к типу bool, за счет потери самих данных
счетчики Counter выгодно применять при подсчете, счетчик имеет фиксированный размер для текущего набора данных



Выводы можно сделать такие, стараться уменьшать количество промежуточных "константных" списков,
 в случае если приходится их использовать - использовать не списки, а кортежи.
 если есть уверенность что сами данные не нужны, приводить к типу bool и подсчитывать в counter
 

"""
