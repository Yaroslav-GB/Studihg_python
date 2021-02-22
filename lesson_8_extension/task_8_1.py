"""

1. Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать
два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй,
с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
структуры на реальных данных.


"""


class Data:

    def __init__(self, data):
        self.data = data

    @classmethod
    def extract_type_int(cls, data):
        day, month, year = map(int, data.split('-'))
        return {'Число': day, 'Месяц': month, 'Год': year}

    @staticmethod
    def valid_date(data):
        day, month, year = map(int, data.split('-'))
        if day in range(32):
            if month in range(13):
                if year in range(9999):
                    return {'Число': day, 'Месяц': month, 'Год': year}
                else:
                    return False
            else:
                return f'Введен несуществующий месяц'
        else:
            return f'Введено несуществующее число месяца'


date_start = '14-02-2021'
date_wrong = '14-14-2021'

print(Data.extract_type_int(date_start))
print(Data.valid_date(date_start))
print('\n')
print(Data.extract_type_int(date_wrong))
print(Data.valid_date(date_wrong))
