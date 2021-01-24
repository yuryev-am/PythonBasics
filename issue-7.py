"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


# Комплексное число вида a + bi. a - действительная часть числа, а b - мнимая часть числа.
class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        # Складываем два комплексных числа вида: a + bi и c + di
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        return ComplexNumber(a + b, c + d)

    def __mul__(self, other):
        # Умножаем два комплексных числа вида: a + bi и c + di
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        return ComplexNumber(a * c - b * d, a * d + b * c)

    def __str__(self):
        return f'{self.a} + {self.b}i'


complex_num_1 = ComplexNumber(3, 5)
complex_num_2 = ComplexNumber(2, 7)

print(complex_num_1)
print(complex_num_2)

print(f'Сложеение: {complex_num_1 + complex_num_2}')
print(f'Умножение: {complex_num_1 * complex_num_2}')
