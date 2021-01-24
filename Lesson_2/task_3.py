"""
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
    digit = cut_digit(number)
    tmp_number = number // 10
    return str(digit) + reverse_number(tmp_number)


num = int(input('Введите целое число'))

print(reverse_number(num))
