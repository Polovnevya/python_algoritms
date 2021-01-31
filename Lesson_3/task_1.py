"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""
START = 0
END = 100
for base in range(2, 10):
    array = [el for el in range(START, END, base) if el >= base and el <= END]
    print(array)
    print(f'В диапазоне {START} - {END} находится {len(array)} чисел кратных {base}')
