"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

digit = int(input('Введите целое трехзначное число'))

first_digit = digit // 100
second_digit = digit // 10 % 10
third_digit = digit % 10

sum_digits = first_digit + second_digit + third_digit
multiply_digits = first_digit * second_digit * third_digit

print(f'Сумма цифр числа {digit} = {sum_digits}')
print(f'Произведение цифр числа {digit} = {multiply_digits}')
