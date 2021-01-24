"""
Здесь в одном файле сразу все заданий с 4 по 6. Делать по сути 3 одинаковых файла, а потом играть в игру
"Найди 10 отличий" такое себе удовольствие)
"""

from abc import ABC, abstractmethod


class StorageCountException(Exception):
    def __init__(self, mess):
        self.mess = mess


class OfficeEquipment(ABC):
    def __init__(self, name: str, price: float, weight: float):
        self.name = name
        self.price = price
        self.weight = weight

    # Так и не придумал какой нормальный метод абстрактный можно сделать, поэтому вот...)
    @abstractmethod
    def __str__(self):
        pass


class Printer(OfficeEquipment):
    """
    printer_type - тип принтера (Струйный или Лазерный)
    print_speed - скорость печати Стр/Мин
    """

    def __init__(self, name: str, price: float, weight: float, printer_type: str, print_speed: int):
        super().__init__(name, price, weight)
        self.printer_type = printer_type
        self.print_speed = print_speed

    def __str__(self):
        return f'Имя: {self.name}, Цена: {self.price}, Вес: {self.weight}, Тип принтера: {self.printer_type}, ' \
               f'Скорость печати: {self.print_speed}'


class Scanner(OfficeEquipment):
    def __init__(self, name: str, price: float, weight: float, scanner_type: str):
        super().__init__(name, price, weight)
        self.scanner_type = scanner_type

    def __str__(self):
        return f'Имя: {self.name}, Цена: {self.price}, Вес: {self.weight}, Тип сканера: {self.scanner_type}'


class Xerox(OfficeEquipment):
    def __init__(self, name: str, price: float, weight: float, xerox_type: str):
        super().__init__(name, price, weight)
        self.xerox_type = xerox_type

    def __str__(self):
        return f'Имя: {self.name}, Цена: {self.price}, Вес: {self.weight}, Тип ксерокса: {self.xerox_type}'


class TechStorage:
    """
    name - наименование склада
    volume - количество мест на складе для товара
    """

    def __init__(self, name: str, volume: int):
        self.name = name
        self.volume = volume
        self.__items_count = 0
        self.__company_division = {}
        self.items = []

    def add_equipment(self, equip: OfficeEquipment, division: str):
        # Для примера добавим проверку общего количества товаров на складе при добавлении товара
        if self.__items_count >= self.volume:
            print(f'Не удалось добавить на склад товар "{equip.name}"')
            raise StorageCountException('На складе закончилось место!')
        else:
            if not self.__company_division.get(division):
                self.__company_division[division] = [equip]
            else:
                self.__company_division[division].append(equip)
            self.items.append(equip)
            self.__items_count += 1
            print(f'Товар "{equip.name}" успешно добавлен на склад')

    @property
    def items_count(self):
        return self.__items_count

    @property
    def company_divisions(self):
        return self.__company_division


# Нус, поработаем с хранилищем нашим

MyStorage = TechStorage('Моя прелесть', 5)

printer1 = Printer('HP 1221', 15999, 3.5, 'Лазерный', 120)
scanner1 = Scanner('Canon BR2312', 32999, 2.8, 'Планшетный')
xerox1 = Xerox('Epson L3151 ', 15990, 3.9, 'Струйный цветной с СНПЧ')

MyStorage.add_equipment(printer1, 'Бухгалтерия')
MyStorage.add_equipment(scanner1, 'Программисты')
MyStorage.add_equipment(scanner1, 'Канцелярия')
MyStorage.add_equipment(xerox1, 'Программисты')
MyStorage.add_equipment(scanner1, 'Бухгалтерия')

# Для проверки исключения в случае если на складе всего 5 мест:
try:
    MyStorage.add_equipment(scanner1, 'Канцелярия')
except StorageCountException as e:
    print(e)

print(f'На складе "{MyStorage.name}" товаров: {MyStorage.items_count}')

for el in MyStorage.items:
    print(el)

print(MyStorage.company_divisions)
