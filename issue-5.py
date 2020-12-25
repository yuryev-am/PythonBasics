# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться
# после них.

rating = [9, 7, 6, 3, 2]
print(f'Изначальное представление рейтинга: {rating}\n')

# Решил попробовать сделать бесконечный цикл ввода значения до тех пор, пока не будет введено корректное значение.
# Однако, PyCharm предупреждает, что переменная new_rating_el после этого цикла может быть неопределена.
# Поэтому, я добавил перед циклом ей значение по умолчанию. Не очень понимаю, почему он ругается.
# Вроде из этого цикла можно выйти только если переменная будет определена. Или я чего-то не вижу.
new_rating_el = 1
while True:
    try:
        new_rating_el = int(input('Введите новый элемент рейтинга (только натуральные числа): '))
    except Exception as e:
        print(e)
        print('Вы ввели не натуральное число. Попробуйте еще раз.')
        continue

    if new_rating_el <= 0:
        print('Вы ввели не натуральное число. Натуральное число не может быть меньше либо равно 0. Попробуйте еще раз.')
        continue

    # Рассмотрим 3 варианта.
    # Первый. Когда введенный элемент больше чем первый в рейтинге.
    if new_rating_el > rating[0]:
        rating.insert(0, new_rating_el)
    # Второй. Когда введенный элемент меньше последнего в рейтинге.
    elif new_rating_el <= rating[-1]:
        rating.append(new_rating_el)
    # Третий. Когда похожий элемент надо искать внутри.
    else:
        for ind, el in enumerate(rating[::-1]):
            # print(ind, el)
            if el == new_rating_el:
                rating.insert(-1 * ind, new_rating_el)
                break
            elif el > new_rating_el:
                rating.insert(-1 * ind, new_rating_el)
                break
    print(f'Новое представление рейтинга: {rating}')
    q = input('Хотите продолжить? (Y, N): ')
    if q.upper() == 'N':
        break
