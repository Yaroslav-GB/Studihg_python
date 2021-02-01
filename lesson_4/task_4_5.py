"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().

"""

from random import randrange
from functools import reduce

rand_list = [randrange(10, 1001, 2) for i in range(901)]



print(f"Список четныx чисeл от 100 до 1000: {rand_list}")

print(f"Произведение всех элементов списка: {reduce(lambda n1, n2: n1 * n2, rand_list)}")
def composit_of_rand_list(el1, el2):                                #для проверки первой функции
    return el1 * el2
print(f"Произведение всех элементов списка: "
      f"{reduce(composit_of_rand_list, [el for el in rand_list])}") #для проверки первой функции