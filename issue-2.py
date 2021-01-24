"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class MyDivisionByZeroException(Exception):
    def __init__(self, txt):
        self.txt = txt


a, b = input('Введите делимое и делитель через пробел: ').split()

try:
    if int(b) == 0:
        raise MyDivisionByZeroException('Делить на 0 нельзя!')
    else:
        print(f'a/b = {int(a) / int(b)}')
except MyDivisionByZeroException as e:
    print(e)
