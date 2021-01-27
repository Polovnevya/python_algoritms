"""
#рекурсивный алгоритм
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.

"""


def row_summ(n: int, start: float) -> float:
    summ = 0
    if n != 0:
        if start == 1:
            summ = 1
            summ = summ + row_summ(n - 1, start / 2 * -1)
            return summ
        else:
            summ = summ + row_summ(n - 1, start / 2 * -1)
            return summ + start
    else:
        return 0


print(f'Программа производит сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…')
n = int(input('Количество элементов (n) '))

print(f'Сумма ряда 1, -0.5, 0.25, -0.125,… c {n} элементамми равна {row_summ(n, 1)}')
