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


def sieve(num: int) -> int:
    """
    ехал грека через список
    """

    assert num < 100, 'больше сотого числа не ищем, извините'

    START = 2
    END = 1_000
    sieve_count = 0
    sieve_array = [i for i in range(START, END)]

    def _pierce_sieve(user_list: list) -> list:
        for el_i in user_list:
            if el_i is not None:
                for el_j in user_list:
                    if el_j is not None and el_j % el_i == 0 and el_j != el_i:
                        index_j = user_list.index(el_j)
                        user_list[index_j] = None
        return user_list

    pierced_sieve_array = _pierce_sieve(sieve_array)

    for value_i in pierced_sieve_array:
        if value_i is not None and sieve_count <= num:
            sieve_count += 1
            if sieve_count == num:
                return value_i


user_num = int(input('Введите какое по счету простое число требуется найти: '))
print(f'Простое число под номером {user_num} это {sieve(user_num)}')
