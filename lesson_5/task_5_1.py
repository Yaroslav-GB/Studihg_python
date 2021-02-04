"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

"""

new_list = []
while True:
    user_list = input("Введите данные(для завершения ввода нажмите пробел): ")
    if user_list == " ":
        break
    else:
        new_list.append(user_list + "\n")

fp = open("task_1_file.txt", "w", encoding="utf-8")
fp.writelines(new_list)
fp.close()

with open("task_1_file.txt", "r", encoding="utf-8") as fp:
    for line in fp:
        print(line)