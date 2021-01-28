"""


3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.


"""

num1 = int(input("Введите первое чило для вычеслений "))
num2 = int(input("Введите второе чило для вычеслений "))
num3 = int(input("Введите третье чило для вычеслений "))


def sumOfMax(a, b, c):
    numlist = [num1, num2, num3]
    return sum(numlist, - min(numlist))


print(sumOfMax(num1, num2, num3))
