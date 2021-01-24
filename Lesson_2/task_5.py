"""
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
    Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


def print_pair(char_code: int) -> None:
    print(f'"{chr(char_code)}" - {char_code}', end='   ')
    return None


def print_row(pair_number: int, char_code: int) -> None:
    print_pair(char_code)
    if pair_number != 1:
        print_row(pair_number - 1, char_code + 1)
        return None
    else:
        print('')


def print_table(char_code, row_num):
    print_row(10, char_code)


start = 32
row_num = (127 - 32) / 10
print_row(10, 32)
