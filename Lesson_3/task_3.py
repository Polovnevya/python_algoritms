"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import randint

MIN_ITEM = 0
MAX_ITEM = 100
SIZE = 10
array = [randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]

min_val = array[0]
min_index = 0
max_val = array[0]
max_index = 0

print('Исходный массив')
print(array)

for i, val in enumerate(array):
    if val > max_val:
        max_val = val
        max_index = i
    elif val < min_val:
        min_val = val
        min_index = i

print(f'Максимальный элемент массива {max_val} с индексом {max_index}')
print(f'Минимальный элемент массива {min_val} с индексом {min_index}')
array[max_index] = min_val
array[min_index] = max_val
print('Измененный массив')
print(array)
