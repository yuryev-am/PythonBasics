"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    date_str = '0-0-0'

    def __init__(self, date_str: str):
        Date.date_str = date_str

    @classmethod
    def date_numb_type(cls):
        cls.d, cls.m, cls.y = cls.date_str.split('-')
        print(f'{cls.d}  {cls.m}  {cls.y}')

    @staticmethod
    def valid_date(date_str):
        d, m, y = date_str.split('-')
        d = int(d)
        m = int(m)
        y = int(y)
        if d < 1 or d > 31:
            print('Число указано не верно!')
        if m < 1 or m > 12:
            print('Месяц указан не верно!')
        if y < 1:
            print('Год указан не верно!')


my_date = Date('1-2-12')
Date.date_numb_type()

my_date1 = Date('21-12-123')
Date.date_numb_type()

# Вызов статического метода. Т.к данный метод ничего не знает про класс и тем более его экземпляр, передаем дату в него
# отдельно
Date.valid_date('1-2-12')
