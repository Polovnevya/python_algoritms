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


def rate_count(number):
    rate = 1
    if number != 0:
        tmp_number = number // 10
        rate = rate + rate_count(tmp_number)
        return rate
    else:
        return 0


def reverse_number(number: int, rate: int) -> int:
    if number != 0:
        digit = cut_digit(number) * 10 ** (rate-1)
        tmp_number = number // 10
        new_number = digit + reverse_number(tmp_number, rate - 1)
        return new_number
    else:
        return 0


num = int(input('Введите целое число '))

print(f'Число после реверса {reverse_number(num, rate_count(num))}')
