"""

5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних
класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный
метод для каждого экземпляра.

"""

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'{self}'

    def __str__(self):
        return f'{self.title}'



pencil = Stationery('pencil')
pencil.title = 'Карандашем'

pen = Stationery('pen')
pen.title = 'Ручкой'

handle = Stationery('handle')
handle.title = 'Маркером'

print(f'Запуск отрисовки {pencil.draw()}')
print(f'Запуск отрисовки {pen.draw()}')
print(f'Запуск отрисовки {handle.draw()}')

