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

    assert num <= 11_000, 'Извините, число больше 11000 не ищем'

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
    assert num <= 11_000, 'Извините, число больше 1100 не ищем'

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

print(timeit('sieve(10)', number=100, globals=globals()))  # 0.0220353
print(timeit('sieve(100)', number=100, globals=globals()))  # 1.3815776
print(timeit('sieve(500)', number=100, globals=globals()))  # 30.284424100000003
print(timeit('sieve(1500)', number=100, globals=globals()))  # 263.7983361
print(timeit('sieve(2500)', number=100, globals=globals()))  # 663.8547732

run('sieve(1500)')
"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    2.362    2.362 <string>:1(<module>)
        1    0.000    0.000    2.362    2.362 task_2.py:18(sieve)
        1    0.001    0.001    0.001    0.001 task_2.py:28(<listcomp>)
        1    0.736    0.736    2.361    2.361 task_2.py:30(_pierce_sieve)
        1    0.000    0.000    2.362    2.362 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    13244    1.626    0.000    1.626    0.000 {method 'index' of 'list' objects}
"""
print('*****************')

print(timeit('prime(10)', number=100, globals=globals()))  # 0.0016482999999425374
print(timeit('prime(100)', number=100, globals=globals()))  # 0.13568280000004052
print(timeit('prime(500)', number=100, globals=globals()))  # 5.76559050000003
print(timeit('prime(1500)', number=100, globals=globals()))  # 62.053306999999904
print(timeit('prime(2500)', number=100, globals=globals()))  # 185.17176159999985
run('prime(1500)')
"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.510    0.510 <string>:1(<module>)
        1    0.002    0.002    0.510    0.510 task_2.py:50(prime)
    12553    0.508    0.000    0.508    0.000 task_2.py:60(_is_prime)
        1    0.000    0.000    0.510    0.510 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

"""
Первый вариант имеет квадратичную зависимость, втроенный метод списков index очень затратный 
Второй вариант ближе к линейному, нечто среднее, 1,5
"""
