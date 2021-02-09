"""
7. Создать (не программно) текстовый файл, в котором каждая строка
должна содержать данные о фирме: название, форма собственности,
выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней
прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами
и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
{“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.

"""
import json
profit_list_for_average = []
firm_list = []
profit_list = []

with open("task_7_file.txt", "r", encoding="utf8") as fp:
    for line in fp:
        firm, ownership, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        firm_list.append(firm)
        profit_list.append(profit)
        if profit > 0:
            profit_list_for_average.append(profit)
        else:
            pass

average_profit = {'average_profit': round(sum(map(int, profit_list_for_average))
                           / len(profit_list_for_average))}

with open("task_7_file.json", "w") as fp:
    json.dump(dict(zip(firm_list, profit_list)), fp)

with open("task_7_file.json", "r") as fp:
    data = json.load(fp)
    print([data, average_profit])

