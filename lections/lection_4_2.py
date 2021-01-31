##############    ПРИМЕР 1
# код проверки(идентификации) запроса у пользователя

data = []

while True:
    userData = input()
    if userData == 'q':
        break
    data.append(userData)
    print(data)
"""РЕЗУЛЬТАТ
ввожу 1
['ввожу 1']
ввожу 2
['ввожу 1', 'ввожу 2']
ввожу 3
['ввожу 1', 'ввожу 2', 'ввожу 3']
й
['ввожу 1', 'ввожу 2', 'ввожу 3', 'й']
q
"""
# упрощенная конструкция, но нет break

while userData := input():
    data.append(userData)
    print(data)

##############    ПРИМЕР 2

if len(list) % 2 == 0:
    xxx = len(list)
else:
    xxx = len(list) - 1

i = 0
while i < xxx:
    m = list[i]
    list[i] = list[i + 1]
    list[i + 1] = m
    i +=2

