"""
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
    Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


def print_pair(char_code: int) -> None:
    print(f'"{chr(char_code)}" - {char_code}')
    return None


def print_row(pair_number: int, char_code: int) -> None:
    print_pair(char_code)
    if pair_number != 0:
        print_row(pair_number - 1, char_code + 1)
        return None


start = 32

print_row(10, start)
