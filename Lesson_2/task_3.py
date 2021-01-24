"""
#рекурсивный алгоритм
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
    Например, если введено число 3486, надо вывести 6843.
"""


def cut_digit(number: int) -> int:
    """
    отрезает последнюю цифру от числа
    :param number: целое натуральное
    :return: возвращает последнюю цифру от числа
    """
    digit = number % 10
    return digit


def reverse_number(number: int) -> int:
    if number != 0:
        digit = cut_digit(number)
        tmp_number = number // 10
        return str(digit) + str(reverse_number(tmp_number))
    else:
        return ""


num = int(input('Введите целое число '))

print(f'Число после реверса {reverse_number(num)}')
