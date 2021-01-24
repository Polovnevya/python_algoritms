"""
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
    Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


def print_pair(char_code: int) -> None:
    print(f'"{chr(char_code)}" - {char_code:^4}  ', end='   ')
    return None


def print_row(pair_number: int, char_code: int) -> None:
    if char_code >= 32 and char_code <= 127:
        print_pair(char_code)
        if pair_number != 1:
            print_row(pair_number - 1, char_code + 1)
            return None
        else:
            print('')
    else:
        return None


def print_table(char_code: int, row_num):
    print_row(10, char_code)
    if row_num != 0:
        print_table(char_code + 10, row_num - 1)


start = 32
row_num = round((127 - 32) / 10)
print_table(32, row_num)
