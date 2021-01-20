"""
По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
    составленного из этих отрезков
https://drive.google.com/file/d/1Ui2yipbPwl4C9ZbY4KEk6VSmB2YBMh-k/view?usp=sharing
"""
segment_1 = float(input('Введите длинну первого отрезка '))
segment_2 = float(input('Введите длинну второго отрезка '))
segment_3 = float(input('Введите длинну третьего отрезка '))

if segment_1 + segment_2 <= segment_3 or segment_2 + segment_3 <= segment_1 or segment_1 + segment_3 <= segment_2:
    print(f'\nТакого треугольника не существует')
elif segment_1 != segment_2 and segment_1 != segment_3 and segment_2 != segment_3:
    print(f'\nРазносторонний треугольник')
elif segment_1 == segment_2 == segment_3:
    print(f'\nРавносторонний треугольник')
else:
    print(f'\nРавнобедренный треугольник')
