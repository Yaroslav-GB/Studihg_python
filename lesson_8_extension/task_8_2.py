"""

2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.

"""


class Exceptions:

    def __init__(self, divisible, divisor):
        self.divisor = divisor
        self.divisible = divisible

    # @staticmethod
    def div_zero(self, divisible, divisor):
        try:
            print(divisible / divisor)
        except ZeroDivisionError as e:
            print('На ноль делить нельзя')


user_divisible = int(input('Введите делимое число '))
user_divisor = int(input('Введите делитель '))

start = Exceptions(user_divisible, user_divisor)
start.div_zero(user_divisible, user_divisor)
