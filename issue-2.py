"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

with open('issue-2.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()

print(f'Количество строк в файле: {len(lines)}')

for line_number, el in enumerate(lines, 1):
    print(f'Количество слов в строке {line_number}: {len(el.split())}')
