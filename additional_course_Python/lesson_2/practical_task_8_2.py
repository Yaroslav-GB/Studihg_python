def to_get_num():
    i = 1
    user_list = []
    while i <= 3:
        user_num = input("Введите число ")
        user_list.append(user_num)
        i += 1
    return user_list


print(max(to_get_num()))
# print(max(int(map(to_get_num()))))
