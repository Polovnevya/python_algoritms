""""
Задача считается решённой, если в ней использована как минимум одна коллекция из модуля collections.

Пользователь вводит данные о количестве предприятий,
    их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
    чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple

Company = namedtuple('Company',
                     'company_name, quarter_profit_1, quarter_profit_2, quarter_profit_3 , quarter_profit_4 avg')


def avg_profit(company: namedtuple) -> namedtuple:
    summ = company.quarter_profit_1 + company.quarter_profit_2 + company.quarter_profit_3 + company.quarter_profit_4
    company = company._replace(avg=summ / 10)
    return company


def get_data_from_user(num: int) -> namedtuple:
    spam = Company(
        input(f'Введите название предприятия №{num}: '),
        float(input('Введите прибыль первого квартала: ')),
        float(input('Введите прибыль второго квартала: ')),
        float(input('Введите прибыль третьего квартала: ')),
        float(input('Введите прибыль четвертого квартала: ')),
        float(0)
    )
    return avg_profit(spam)


def get_and_print_company_data(count: int):
    company_num = []
    total_avg = 0
    for i in range(1, count + 1):
        company_num.append(get_data_from_user(i))
        total_avg += company_num[i - 1].avg
    total_avg = total_avg / count

    for i in range(1, count + 1):
        if company_num[i - 1].avg > total_avg:
            more_less = 'выше'
        else:
            more_less = 'ниже'
        print(f'Компания "{company_num[i - 1].company_name}" имеет среднюю прибыль {company_num[i - 1].avg}'
              f' {more_less} средней прибыли всех предприятий {total_avg}')


get_and_print_company_data(2)
