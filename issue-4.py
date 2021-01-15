"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self):
        self.speed = 0
        self.color = None
        self.name = None
        self.is_police = False
        # Сделал эту переменную чтобы убрать ворнинги PyCharm. Он все хотел метот turn сделать статичным.
        self.direction = 'Прямо'

    def go(self):
        print(f'Машина поехала со скоростью {self.speed} км/ч')

    def stop(self):
        self.speed = 0
        print('Машина остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super(TownCar, self).show_speed()
        if self.speed > 60:
            print('Машина привысила скорость 60 км/ч')


class WorkCar(Car):
    def show_speed(self):
        super(WorkCar, self).show_speed()
        if self.speed > 40:
            print('Машина привысила скорость 40 км/ч')


class SportCar(Car):
    def show_speed(self):
        super(SportCar, self).show_speed()
        if self.speed > 100:
            print('Машина привысила скорость 100 км/ч')


class PoliceCar(Car):
    def __init__(self):
        super(PoliceCar, self).__init__()
        self.is_police = True

    def show_speed(self):
        super(PoliceCar, self).show_speed()


newCar = TownCar()
newCar.speed = 70
newCar.color = 'Red'
newCar.name = 'Lada Granta'
print(f'Имя машины: {newCar.name}. Цвет машины: {newCar.color} Машина полицейская?: {newCar.is_police}')
newCar.go()
newCar.turn('на право')
newCar.turn('на лево')
newCar.show_speed()
newCar.stop()
print('\n')

newCar1 = WorkCar()
newCar1.speed = 70
newCar1.color = 'Blue'
newCar1.name = 'Honda'
print(f'Имя машины: {newCar1.name}. Цвет машины: {newCar1.color} Машина полицейская?: {newCar1.is_police}')
newCar1.go()
newCar1.turn('на право')
newCar1.show_speed()
newCar1.stop()
print('\n')

newCar2 = SportCar()
newCar2.speed = 120
newCar2.color = 'Yellow'
newCar2.name = 'Ferrari'
print(f'Имя машины: {newCar2.name}. Цвет машины: {newCar2.color} Машина полицейская?: {newCar2.is_police}')
newCar2.go()
newCar2.turn('на право')
newCar2.show_speed()
newCar2.stop()
print('\n')

newCar3 = PoliceCar()
newCar3.speed = 120
newCar3.color = 'Black'
newCar3.name = 'lamborghini gallardo'
print(f'Имя машины: {newCar3.name}. Цвет машины: {newCar3.color} Машина полицейская?: {newCar3.is_police}')
newCar3.go()
newCar3.turn('на лево')
newCar3.show_speed()
newCar3.stop()
