"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс,
описывающий склад. А также класс «Оргтехника», который будет базовым
для классов-наследников. Эти классы — конкретные типы оргтехники
(принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие
за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру,
например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации
вводимых пользователем данных. Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              1. Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать
два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй,
с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
структуры на реальных данных.

начало ----> получение твоара ----> хранение и учет ----> выдача товара ----> конец
"""


class OfficeEquipment:
    def __init__(self, name, model):
        self.name = name
        self.model = model


class Storage():
    def __init__(self, type):
        self.type = type
        if self.type == 'принтер':
            self.to_take_printer_from_txt()
        elif self.type == 'сканер':
            self.to_take_scanner_from_txt()
        elif self.type == 'ксерокс':
            self.to_take_copier_from_txt()

    def to_take_printer_from_txt(self):
        with open("printer_file.txt", "r", encoding="utf-8") as fp:
            with open("printer_file_inventory.txt", "w", encoding="utf-8") as fp2:
                storage_list = []
                for line in fp:
                    line = line.split('\n')
                    for i in line:
                        if i != '':
                            storage_list.append(i + ',')
                    user_inventory = input('Введите присваиваемы инвентарный номер: \n')
                    user_dept = input('Введите к какому отделу прикрепить: \n')
                    storage_list.append(user_inventory + ',' + user_dept + '\n')
                fp2.writelines(storage_list)

    def to_take_scanner_from_txt(self):
        storage_list = []
        with open("scanner_file.txt", "r", encoding="utf-8") as fp:
            with open("scanner_file_inventory.txt", "w", encoding="utf-8") as fp2:
                for line in fp:
                    line = line.split('\n')
                    for i in line:
                        if i != '':
                            storage_list.append(i + ',')
                    user_inventory = input('Введите присваиваемы инвентарный номер: \n')
                    user_dept = input('Введите к какому отделу прикрепить: \n')
                    storage_list.append(user_inventory + ',' + user_dept + '\n')
                fp2.writelines(storage_list)

    def to_take_copier_from_txt(self):
        storage_list = []
        with open("copier_file.txt", "r", encoding="utf-8") as fp:
            with open("copier_file_inventory.txt", "w", encoding="utf-8") as fp2:
                for line in fp:
                    line = line.split('\n')
                    for i in line:
                        if i != '':
                            storage_list.append(i + ',')
                    user_inventory = input('Введите присваиваемы инвентарный номер: \n')
                    user_dept = input('Введите к какому отделу прикрепить: \n')
                    storage_list.append(user_inventory + ',' + user_dept + '\n')
                fp2.writelines(storage_list)


class Printer(OfficeEquipment):

    @staticmethod
    def to_take_data_equipment(self):
        equipment_list = []
        q = 1
        try:
            user_insert_quantity = int(input("Введите количесвто добавляемой техники: \n"))
        except ValueError as e:
            int(input("Вы ввели не число. Введите количество в штуках: \n"))
        while q <= user_insert_quantity:
            user_insert_name = input("Введите марку принтера: \n")
            equipment_list.append(user_insert_name + ',')
            user_insert_model = input("Введите модель принтера: \n")
            equipment_list.append(user_insert_model + '\n')
            q += 1

        fp = open("printer_file.txt", "w", encoding="utf-8")
        fp.writelines(equipment_list)
        fp.close()


class Scanner(OfficeEquipment):

    @staticmethod
    def to_take_data_equipment(self):
        equipment_list = []
        q = 1
        try:
            user_insert_quantity = int(input("Введите количесвто добавляемой техники: \n"))
        except ValueError as e:
            int(input("Вы ввели не число. Введите количество в штуках: \n"))
        while q <= user_insert_quantity:
            user_insert_name = input("Введите марку сканера: \n")
            equipment_list.append(user_insert_name + ',')
            user_insert_model = input("Введите модель сканера: \n")
            equipment_list.append(user_insert_model + '\n')
            q += 1

        fp = open("scanner_file.txt", "w", encoding="utf-8")
        fp.writelines(equipment_list)
        fp.close()


class Copier(OfficeEquipment):

    @staticmethod
    def to_take_data_equipment(self):
        equipment_list = []
        q = 1
        try:
            user_insert_quantity = int(input("Введите количесвто добавляемой техники: \n"))
        except ValueError as e:
            int(input("Вы ввели не число. Введите количество в штуках: \n"))
        while q <= user_insert_quantity:
            user_insert_name = input("Введите марку ксерокса: \n")
            equipment_list.append(user_insert_name + ',')
            user_insert_model = input("Введите модель ксерокса: \n")
            equipment_list.append(user_insert_model + '\n')
            q += 1

        fp = open("copier_file.txt", "w", encoding="utf-8")
        fp.writelines(equipment_list)
        fp.close()


def adding_equipment_to_storage():
    while True:
        user_insert_equipment = input('Укажите, что будем добавлять на склад:'
                                      ' принтер, сканер, ксерокс? \n'
                                      '(для завершения введите пробел) \n').lower()
        if user_insert_equipment == " ":
            break
        elif user_insert_equipment == 'принтер':
            Printer.to_take_data_equipment(user_insert_equipment)
        elif user_insert_equipment == 'сканер':
            Scanner.to_take_data_equipment(user_insert_equipment)
        elif user_insert_equipment == 'ксерокс':
            Copier.to_take_data_equipment(user_insert_equipment)
        else:
            input('Вы ввели неправильное наименование техники. \n'
                  'Укажите: принтер, сканер или ксерокс.'
                  'Для завершения введите пробел пробел. \n').lower()


def to_start_inventory_equipment():
    while True:
        user_extract_equipment = (input('Укажите, что достать '
                                        'из склада для инветаризации:'
                                        ' принтер, сканер, ксерокс?\n'
                                        'Для завершения введите пробел\n').lower())

        if user_extract_equipment == " ":
            break
            to_enumerate_content_storage()
        elif user_extract_equipment == 'принтер' or 'сканер' or 'ксерокс':
            Storage(user_extract_equipment)



def to_chek_equipment_inventoried_storage():
    with open("printer_file_inventory.txt", "r", encoding="utf-8") as fp_p:
         with open("scanner_file_inventory.txt", "r", encoding="utf-8") as fp_s:
            with open("copier_file_inventory.txt", "r", encoding="utf-8") as fp_c:
                with open("equipment_total_file.txt", "a+", encoding="utf-8") as fp_total:
                    fp_total.writelines(fp_p)
                    fp_total.writelines(fp_s)
                    fp_total.writelines(fp_c)


def to_enumerate_content_storage():
    with open("equipment_total_file.txt", "r", encoding="utf-8") as fp:
        for line in enumerate(fp, 1):
            print(f'На складе сейчас зарегистрирована следующая техника: \n{line}')

adding_equipment_to_storage()
to_start_inventory_equipment()
to_chek_equipment_inventoried_storage()
to_enumerate_content_storage()

