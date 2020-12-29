# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее
# сумме и после этого завершить программу.

def f_my_sum(val_lst):
    """
    Функция суммы значений списка. Если в списке есть значения, не являющиеся числами, то они пропускаются
    :param val_lst: Список значений для сложения
    :return: сумма значений элементов списка
    """
    s = 0
    for el in val_lst:
        try:
            s += float(el)
        except ValueError:
            continue
    return s


my_sum = 0
while True:
    values_list = input(f'Введите числа, разделенные пробелом (Для выхода введите символ "q"): ').split()
    print(values_list)
    my_sum += f_my_sum(values_list)
    print(f'Общая сумма: {my_sum}')
    if 'q' in values_list:
        break
