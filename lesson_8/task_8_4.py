"""

4. Начните работу над проектом «Склад оргтехники». Создайте класс,
описывающий склад. А также класс «Оргтехника», который будет базовым
для классов-наследников. Эти классы — конкретные типы оргтехники
(принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

"""


class OfficeEquipment:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def __str__(self):
        return f"Марки: {self.name}; Модель: {self.model}"


class Storage():
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Cклад: {self.name}; Адрес: {self.address}"

    def assign_inventory(self, quantity, *equipments):
        for eq in equipments:
            eq.to_take_quants(quantity)


class Printer(OfficeEquipment):

    def __init__(self, name, model):
        super().__init__(name, model)
        self.quantities = []

    def to_take_quants(self, quantity):
        self.quantities.append(quantity)

    @staticmethod
    def name_of_equipment(self):
        return self


class Scanner(OfficeEquipment):

    def __init__(self, name, model):
        super().__init__(name, model)
        self.quantities = []

    def to_take_quants(self, quantity):
        self.quantities.append(quantity)

    @staticmethod
    def name_of_equipment(self):
        return self


class Copier(OfficeEquipment):

    def __init__(self, name, model):
        super().__init__(name, model)
        self.quantities = []

    def to_take_quants(self, quantity):
        self.quantities.append(quantity)

    @staticmethod
    def name_of_equipment(self):
        return self


import random


class Inventory:
    def __init__(self, *quantities):
        self.quantities = quantities

    def inventory_management(self):
        for el in self.quantities:
            return random.choice(el)  # не доработал присваивание инвентарного номера. поставил рандом


inventory = Inventory("78964")
storage = Storage('ООО "Офисная Техника"', 'Москва МКАД, 46км')

printer = Printer("HP", " LaseJet")
scanner = Scanner("Epson", " Perfection V19")
copier = Copier("Xerox", "WorkCentre 3025NI")

(storage.assign_inventory(inventory, printer, scanner, copier))

print(storage)
print(f'{Printer.name_of_equipment("Принтер")} {printer} в наличии  '
      f'{printer.quantities[0].inventory_management()}шт.')
print(f'{Scanner.name_of_equipment("Сканнер")} {scanner} в наличии  '
      f'{scanner.quantities[0].inventory_management()}шт.')
print(f'{Copier.name_of_equipment("Ксерокс")} {copier} в наличии  '
      f'{copier.quantities[0].inventory_management()}шт.')
