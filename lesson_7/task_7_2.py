"""

2. Реализовать проект расчета суммарного расхода ткани на
производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто)
и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать
формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике
полученные на этом уроке знания: реализовать абстрактные классы

"""
from abc import abstractmethod

consumption = []


class Cloth:

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calc_of_cloth(self):
        print('Расход ткани')


class Coat(Cloth):

    def calc_of_cloth(self):
        super().calc_of_cloth()
        consumption_coat = round(self.param / 6.5 + 0.5, 2)
        consumption.append(consumption_coat)
        return consumption_coat

    def __str__(self):
        return f'для пальто {self.calc_of_cloth()} ед. \n'


class Suit(Cloth):

    def calc_of_cloth(self):
        super().calc_of_cloth()
        consumption_suit = self.param * 2 + 0.3
        consumption.append(consumption_suit)
        return consumption_suit

    def __str__(self):
        return f'для для костюма {self.calc_of_cloth()} ед.\n'


coat = Coat(20)
suit = Suit(30)

print(coat)
print(suit)
print(f'Общий расход ткани составляет: {sum(consumption):.2f} ед.')

# print('"coat" in class Cloth? ', isinstance(coat, Cloth))
# print('"suit" in class Cloth? ', isinstance(suit, Cloth))
