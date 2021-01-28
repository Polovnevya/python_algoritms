"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
from random import randint

MIN_ITEM = 0
MAX_ITEM = 100
COL_PARAM = 5
ROW_PARAM = 5

matrix = [[randint(MIN_ITEM, MAX_ITEM) for _ in range(COL_PARAM)] for _ in range(ROW_PARAM)]

for row in matrix:
    for el in row:
        print(f'{el:^6}', end='')
    print('')

for _ in range(len(matrix[0])):
    print('- - - ', end='')
print('')

min_in_column = []
for j in range(len(matrix[0])):
    for row in matrix:
        if not min_in_column or len(min_in_column) <= j:
            min_in_column.append(row[j])
        elif min_in_column[j] >= row[j]:
            min_in_column[j] = row[j]
    print(f'{min_in_column[j]:^6}', end='')

min_el = 0
for el in min_in_column:
    if min_el < el:
        min_el = el

print('')
print(f'Максимальный элемент среди минимальных элементов столбцов - {min_el}')
