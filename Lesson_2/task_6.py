"""
6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться,
    больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести правильный ответ.
"""

from random import randint


def check_user_num(user_num: int, secret_num: int) -> str:
    if secret_num > user_num:
        return f'Ваше число меньше'
    elif secret_num < user_num:
        return f'Ваше число больше'
    else:
        return f'Победа'


def guess_num(attempt: int, num: int):
    user_num = int(input(f'Угадайте число от 0 до 100, у вас {attempt} попыток '))
    if attempt >= 2:
        if check_user_num(user_num, num) != 'Победа':
            print(check_user_num(user_num, num))
            guess_num(attempt - 1, num)
        else:
            print(f'Вы победили! Было загадано число {num}')
    else:
        print(f'Вы проиграли, было загадано число {num}')


attempt_param = 10
secret_num = randint(0, 100)
guess_num(attempt_param, secret_num)
