##############    генератор списка
#вариант простой
a = [1, 2, 3, 4, 5]
b = [] #b = [1, 4, 9...]
for i in a:
    b.append(i*i)
print(b)
#вариант генератор списка
b = [i*i for i in a]

#вариант генератор словарей
my_dict = {el: el*2 for el in range(10, 20)}
#пример
a = [1, 2, 3, 4, 5]
b = {i: i*i for i in a}
print(b)
"""
result:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""
#вариант генератор множест
my_set = {el**3 for el in range(5, 10)}
#пример
a = [1, 2, 3, 4, 5, 6, 6, 7, 4, 3, 2, 1, 2, 4, 5]
b = {i*i for i in a}
print(b)
"""
result:
{1, 4, 36, 9, 16, 49, 25}
"""

#образец кода generator
a = [1, 2, 3, 4, 5, 6, 6, 7, 4, 3, 2, 1, 2, 4, 5]
g = (x for x in a)

for i in a:
    print(next(g))