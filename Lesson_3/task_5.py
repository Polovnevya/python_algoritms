"""
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""
from random import randint

MIN_ITEM = -10
MAX_ITEM = 10
SIZE = 10
array = [randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]

print(array)
min_max_val = 0
min_max_index = 0
for i, el in enumerate(array):
    if el < 0:
        if el < min_max_val and min_max_val == 0:
            min_max_val = el
            min_max_index = i
        elif el > min_max_val:
            min_max_val = el
            min_max_index = i

print(f'максимальный отрицательный элемент массива {min_max_val} с индексом {min_max_index} ')
