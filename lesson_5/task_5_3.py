"""
3. Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов. Определить, кто из сотрудников имеет
оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
средней величины дохода сотрудников.

"""

with open("task_3_file.txt", "r", encoding="utf-8") as fp:
    fp = list(fp)
    list_of_revenue = []
    div_num = 0
    print("Список сотрудников [фамилия, зарпалата в руб.]: ")
    for i in fp:
        i = i.split()
        div_num +=1
        print(i)
        if int(i[1]) < 20000:
            print(f"\nСотрудник {i[0]} имеет оклад менее 20000р. "
                  f"\nИ составляет: {i[1]} р.")
            list_of_revenue.append(int(i[1]))
        else:
            list_of_revenue.append(int(i[1]))
    print(f"\nСредняя величина дохода сотрудников: "
          f"{round(sum(list_of_revenue)/div_num)}р.")

        #print(r)


