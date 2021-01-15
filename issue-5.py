"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self):
        self.title = None

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
        super(Pen, self).__init__()
        self.title = 'Ручка'

    def draw(self):
        print('Рисуем ручкой')


class Pencil(Stationery):
    def __init__(self):
        super(Pencil, self).__init__()
        self.title = 'Карандаш'

    def draw(self):
        print('Рисуем карандашом')


class Handle(Stationery):
    def __init__(self):
        super(Handle, self).__init__()
        self.title = 'Маркер'

    def draw(self):
        print('Рисуем маркером')


my_pen = Pen()
print(my_pen.title)
my_pen.draw()

print('\n')

my_Pencil = Pencil()
print(my_Pencil.title)
my_Pencil.draw()

print('\n')

my_Handle = Handle()
print(my_Handle.title)
my_Handle.draw()
