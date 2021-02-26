import random

my_num = random.randint(1, 100)
print(f'Мое число: {my_num}')

max_num = 100
min_num = 1

while comp_num != my_num:

    comp_num = random.randint(int(min_num), int(max_num))
    print(f'АИ объявляет число: {comp_num}')
    user_help = input('АИ ждет подсказку ')

    if user_help == '>':
        if comp_num > min_num:
            min_num = comp_num + 1
        ##comp_num = random.randint(int(min_num), int(max_num))
    # print(f'АИ объявляет число: {comp_num}')
    elif user_help == '<':
        if comp_num < max_num:
            max_num = comp_num - 1
        # comp_num = random.randint(int(min_num), int(max_num))
        # print(f'АИ объявляет число: {comp_num}')

else:
    print(f'АИ угадал! И его число: {comp_num}')
