# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_info(first_name, last_name, year_of_birth, city, email, phone):
    """
    Функция получает данные пользователя и выводит их одной строкой
    :param first_name: Имя пользователя
    :param last_name: Фамилия пользователя
    :param year_of_birth: Дата рождения
    :param city: Город
    :param email: электронный почтовый адрес
    :param phone: телефон
    :return: строка с данными пользователя
    """
    return f'Пользователь {last_name} {first_name} родился в {year_of_birth} году, в городе {city}. Email: {email}.' \
           f' Телефон: {phone}'


print(user_info(first_name='Сергей', last_name='Сидоров', year_of_birth=1980, city='Екатеринбург',
                email='sidorov1980Top@gmail.com', phone='+7345325697'))
