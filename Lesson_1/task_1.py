"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
Блок-схема
https://drive.google.com/file/d/1Ui2yipbPwl4C9ZbY4KEk6VSmB2YBMh-k/view?usp=sharing
"""

digit = int(input('Введите целое число от 100 до 999 '))

first_digit = digit // 100
second_digit = digit // 10 % 10
third_digit = digit % 10

sum_digits = first_digit + second_digit + third_digit
multiply_digits = first_digit * second_digit * third_digit

print(f'\nСумма цифр числа {digit} = {sum_digits}')
print(f'Произведение цифр числа {digit} = {multiply_digits}')
