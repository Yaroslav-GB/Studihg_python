#Практическое задание 2 урока
#2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input()

lenOfList = int(input("Введите длину желаемого списка "))
newList = []
i = 0
while i < lenOfList:
    newList.append(input("Введите элемент списка "))
    i += 1
#строки 15-21 списал с методички,
#пока еще недопонял как это работает
list_reverse = ''
symbols = list(newList)
for el in range(len(newList) // 2):
    tmp = symbols[el]
    symbols[el] = symbols[len(newList) - el - 1]
    symbols[len(newList) - el - 1] = tmp
list_reverse = ', ' .join(symbols)
print(f"Ваш список: {newList}")
print(f"Реверс спика: {list_reverse}")