"""
Написать два алгоритма нахождения i-го по счёту простого числа.
 Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
  Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
 Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""

from timeit import timeit
from cProfile import run


def sieve(num: int) -> int:
    """
    ехал грека через список
    """

    assert num <= 10_000, 'Извините, число больше 10000 не ищем'

    START = 2
    END = num * 10
    sieve_count = 0
    sieve_array = [i for i in range(START, END)]

    def _pierce_sieve(user_list: list) -> list:
        for el_i in user_list:
            if el_i is not None:
                for el_j in user_list:
                    if el_j is not None \
                            and el_j % el_i == 0 \
                            and el_j != el_i:
                        index_j = user_list.index(el_j)
                        user_list[index_j] = None
        return user_list

    pierced_sieve_array = _pierce_sieve(sieve_array)

    for value_i in pierced_sieve_array:
        if value_i is not None and sieve_count <= num:
            sieve_count += 1
            if sieve_count == num:
                return value_i


def prime(num: int) -> int:
    """
    модерн
    """
    assert num <= 10_000, 'Извините, число больше 1000 не ищем'

    START = 1
    END = num * 10
    sieve_count = 0

    def _is_prime(num: int) -> bool:
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    for i in range(START, END):
        if _is_prime(i):
            sieve_count += 1
            if sieve_count == num:
                return i


# user_num = int(input('Введите какое по счету простое число требуется найти: '))
# user_num = 3000
# print(f'Простое число под номером {user_num} это {sieve(user_num)}')
# print(f'Простое число под номером {user_num} это {prime(user_num)}')
#
print(timeit('sieve(10)', number=100, globals=globals()))
print(timeit('sieve(100)', number=100, globals=globals()))
print(timeit('sieve(1000)', number=100, globals=globals()))
print(timeit('sieve(9999)', number=100, globals=globals()))

print('*****************')

print(timeit('prime(10)', number=100, globals=globals()))
print(timeit('prime(100)', number=100, globals=globals()))
print(timeit('prime(1000)', number=100, globals=globals()))
print(timeit('prime(9999)', number=100, globals=globals()))
