"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто)
и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Cloth(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def tissue_consumption(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


class Coat(Cloth):
    def __init__(self, name, size):
        super(Coat, self).__init__(name)
        self._V = size

    def tissue_consumption(self):
        return self._V / 6.5 + 0.5


class Suit(Cloth):
    def __init__(self, name, height):
        super(Suit, self).__init__(name)
        self._H = height

    def tissue_consumption(self):
        return self._H * 2 + 0.3


my_coat = Coat('Шикарное пальто', 50)
print(f'Для пальто "{my_coat.name}" нужно {my_coat.tissue_consumption():.3f} ткани')

my_suit = Suit('Любимый костюм', 185)
print(f'Для костюма "{my_suit.name}" нужно {my_suit.tissue_consumption()} ткани')
