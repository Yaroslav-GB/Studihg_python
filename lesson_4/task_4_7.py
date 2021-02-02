"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим
очередное значение. При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить
только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например,
факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

"""
import math
from itertools import count

num_n = int(input("Введите число факториала 'N' "))
list_nums_n = []

def generator_nums_for_factorial():
    a = 1
    b = 0
    while True:
        b += a
        if b <= num_n:
            yield b
        else:
            break


print("Первые 'N' числа факториала: ", end=" ")
for i in generator_nums_for_factorial():
    list_nums_n.append(i)
    print(i, end=" ")

print(f"\nФакториал числа = {num_n}! = {math.factorial(num_n)}")

