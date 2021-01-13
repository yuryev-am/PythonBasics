"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random

# Сгенерируем рандомно числа чтобы заполнить файл
with open('issue-5.txt', 'w') as f:
    for _ in range(10):
        f.write(f'{random.randint(0, 100)} ')

with open('issue-5.txt', 'r') as f:
    numbers = f.readline().split()

# print(numbers)

numbers = [int(numb) for numb in numbers]  # Преобразуем список строк к списку чисел

print(f'Сумма чисел в файле: {sum(numbers)}')
