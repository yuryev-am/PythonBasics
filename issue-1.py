"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
Matrix (двух матриц). Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, lst: list[list]):
        self.lst = lst

    def __str__(self):
        self.__tmp_str = ''
        for el in self.lst:
            for num in el:
                self.__tmp_str += str(num) + '  '
            self.__tmp_str += '\n'
        return self.__tmp_str

    def __add__(self, other):
        if len(self.lst) != len(other.lst) or len(self.lst[0]) != len(other.lst[0]):
            raise ValueError
        else:
            for i in range(len(self.lst)):
                if len(self.lst[i]) != len(other.lst[i]):
                    raise ValueError
        sum_res = []
        for i in range(len(self.lst)):
            sum_res.append([self.lst[i][j] + other.lst[i][j] for j in range(len(self.lst[i]))])
        return Matrix(sum_res)


my_lst = [[1, 2, 4], [3, 5, 6], [1, 7, 4]]
my_lst1 = [[1, 2, 4], [3, 5, 6], [5, 6, 7]]

my_mat = Matrix(my_lst)
my_mat1 = Matrix(my_lst1)

print(my_mat)
print(my_mat1)

print(my_mat + my_mat1)
