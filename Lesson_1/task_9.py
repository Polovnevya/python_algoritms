"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
https://drive.google.com/file/d/1Ui2yipbPwl4C9ZbY4KEk6VSmB2YBMh-k/view?usp=sharing
"""

digit_1 = float(input('Введите первое число '))
digit_2 = float(input('Введите второе число '))
digit_3 = float(input('Введите третье число '))

if digit_2 < digit_1 < digit_3 or digit_2 > digit_1 > digit_3:
    print(f'Число {digit_1} является средним')
elif digit_1 < digit_2 < digit_3 or digit_1 > digit_2 > digit_3:
    print(f'Число {digit_2} является средним')
else:
    print(f'Число {digit_3} является средним')
