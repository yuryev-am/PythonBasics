# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

a = input('Введите целое число: ')
print(a)
i = 0
max_val = 0
while i < len(a):
    if int(a[i]) > max_val:
        max_val = int(a[i])
    if max_val == 9:
        break
    # print(a[i])
    i += 1
print(f'Максимальное число: {max_val}')
