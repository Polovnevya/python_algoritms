"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
https://drive.google.com/file/d/1Ui2yipbPwl4C9ZbY4KEk6VSmB2YBMh-k/view?usp=sharing
"""

char_1 = input('Введите первую букву из диапазона a-z ')
char_2 = input('Введите вторую букву из диапазона a-z ')
char_1_place = ord(char_1) - ord('a') + 1
char_2_place = ord(char_2) - ord('a') + 1
char_num = abs(char_1_place - char_2_place)

print(f'Первая буква {char_1} является {char_1_place} буквой алфавита a-z')
print(f'Вторая буква {char_2} является {char_2_place} буквой алфавита a-z')
print(f'Между буквами {char_1} и {char_2} находится {char_num} букв')
