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


def print_table(char_code: int, row_num, char_in_row):
    print_row(char_in_row, char_code)
    if row_num != 0:
        print_table(char_code + char_in_row, row_num - 1, char_in_row)


first_char_code = 32
last_char_code = 127
char_in_row = 10
row_num = round((last_char_code - first_char_code) / char_in_row)
print_table(first_char_code, row_num, char_in_row)
