"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый
текстовый файл.
"""

numbers_dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('issue-4.txt', 'r', encoding='utf8') as f:
    source_lines = f.readlines()

print(source_lines)

with open('issue-4-new.txt', 'w', encoding='utf8') as f_new:
    for el in source_lines:
        for el_dic in numbers_dic:
            el = el.replace(el_dic, numbers_dic[el_dic])
        f_new.write(el)
