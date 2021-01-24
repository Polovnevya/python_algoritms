""""
Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
    в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def check_even(digit: int) -> bool:
    if digit % 2 == 0:
        return True
    else:
        return False


def cut_digit(number: int) -> int:
    digit = number % 10
    return digit


def cut_and_check_even(number: int):
    digit = cut_digit(number)
    return check_even(digit)


def even_count(number: int) -> int:
    even = 0
    result = 0
    if number != 0:
        if cut_and_check_even(number):
            even = even + 1
        tmp_number = number // 10
        result = even_count(tmp_number)
        return even + result
    else:
        return 0


def odd_count(number: int) -> int:
    odd = 0
    result = 0
    if number != 0:
        if not cut_and_check_even(number):
            odd = odd + 1
        tmp_number = number // 10
        result = odd_count(tmp_number)
        return odd + result
    else:
        return 0


def main(number: int) -> str:
    even = even_count(number)
    odd = odd_count(number)
    return f' в числе {number} находится {even} четных цифры и {odd} нечетных цифр'


num = int(input('Введите натуральное число '))
print(f'{main(num)}')
