"""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque


def hex_sum():
    hex_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


    if first_num < second_num:
        first_num, second_num = second_num, first_num
    third = deque()
    k = 0
    while first_num:
        spam = first_num.pop()
        if second_num:
            ham = second_num.pop()
            egg_index = (hex_num.index(spam) + hex_num.index(ham) + k) % 16
            egg = hex_num[egg_index]
            third.appendleft(egg)
        else:
            egg_index = (hex_num.index(spam) + k) % 16
            egg = hex_num[egg_index]
            third.appendleft(egg)

        if (hex_num.index(spam) + hex_num.index(ham)) >= 15:
            k = 1
        else:
            k = 0
    return third


first_num = deque(input('Введите первое 16ричное число: '))
second_num = deque(input('Введите второе 16ричное число: '))
a = hex_sum()
b = 1
