# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

gain = float(input('Введите значение выручки Вашей Фирмы: '))
costs = float(input('Введите значение издержек Вашей Фирмы: '))
print(f'Выручка: {gain}')
print(f'Издержки: {costs}')

if gain > costs:
    print('Поздравляю, ваша Фирма работает в прибыль!')
    print(f'Рентабельность Фирмы: {(gain - costs) / gain:.2f}')
elif gain < costs:
    print('К сожалению, ваша Фирма работает в убыток.')
else:
    print('Ваша Фирма вышла в ноль! Это не плохо, но надо стараться лучше!')

if gain > costs:
    workers_cnt = int(input('Введите численность вашей Фирмы: '))
    print(f'Прибыль Фирмы на одного сотрудника составляет: {(gain - costs) / workers_cnt}')
