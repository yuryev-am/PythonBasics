"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open('issue-1.txt', 'w') as f:
    while True:
        in_str = input('Введите строку для записи в файл: ')
        if not in_str:
            break
        f.write(f'{in_str}\n')
