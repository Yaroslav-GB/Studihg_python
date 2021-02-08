rus_list = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new_file = []

with open("task_4_file.txt", "r", encoding="utf8") as fp:
    with open("task_4_1_file.txt", "w", encoding="utf8") as fp2:
        for i in fp:
            i = i.split(' ', 1)
            new_file.append(rus_list[i[0]] + ' ' + i[1])
        print(new_file)
        fp2.writelines(new_file)
