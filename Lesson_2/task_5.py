"""
# рекурсивный алгоритм
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
    Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


def print_pair(char_code: int) -> None:
    """
    производит вывод на печать пары - "символ" - Код символа
    :param char_code: принимает код символа
    :return: ничего не возвращает
    """
    print(f'"{chr(char_code)}" - {char_code:^4}  ', end='   ')
    return None


def print_row(pair_number: int, char_code: int) -> None:
    """
    производит печать строки таблицы, для печати пары Символ\код вызывает функцию print_pair
    :param pair_number: количество пар в строке
    :param char_code: код символа с которого надо начинать печать строки
    :return: ничего не возвращает
    """
    if char_code >= 32 and char_code <= 127:
        print_pair(char_code)
        if pair_number != 1:
            print_row(pair_number - 1, char_code + 1)
            return None
        else:
            print('')
    else:
        return None


def print_table(char_code: int, row_num: int, pair_in_row: int) -> None:
    """
    печатает таблицу с парами Символ\код. для печати строки вызывает функцию print_row
    :param char_code: Код символа с которого надо начинать печатать таблицу
    :param row_num: количество строк в таблице
    :param pair_in_row: символов в строке
    :return:
    """
    print_row(pair_in_row, char_code)
    if row_num != 0:
        print_table(char_code + pair_in_row, row_num - 1, pair_in_row)


# Первый символ
first_char_code = 32
# последний символ
last_char_code = 127
# пар в строке
pair_in_row = 10
# количество строк
row_num = round((last_char_code - first_char_code) / pair_in_row)

print_table(first_char_code, row_num, pair_in_row)
