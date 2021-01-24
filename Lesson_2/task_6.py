"""
6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться,
    больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести правильный ответ.
"""

from random import randint

attempt_param = 10
secret_num = randint(0, 101)


def check_user_num(user_num: int, secret_num: int) -> str:
    if secret_num > user_num:
        return f'+'
    elif secret_num < user_num:
        return f'_'
    else:
        return f'='


def guess_num(attempt: int, num: int):
    user_num = int(input(f'Угадайте число от 0 до 100, у вас {attempt} попыток '))
    if attempt > 0:
        print (check_user_num(user_num, num))
    else:
        print(f'Вы проиграли, было загадано число {num}')
