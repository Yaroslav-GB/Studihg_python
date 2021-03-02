import random

random_num = random.randint(1, 100)
print(random_num)

user_num = None
attempt = 0

levels = {1: 10, 2: 5, 3: 3}
level = int(input('Введит уровень сложности от 1 до 3 '))
max_attempt = levels[level]

quantity_players = int(input('Введите количество игроков '))
players = []
for i in range(quantity_players):
    player_name = input(f'Введите имя игрока №{i + 1}: \n')
    players.append(player_name)

print(f'Ваш уровень сложности:{level} и у вас есть {levels[level]} попыток.')

is_winner = False
winner_name = None

while not is_winner:
    attempt += 1
    if attempt > max_attempt:
        print('Вы проиграли')
        break
    print(f'Поппытка №{attempt}')
    for player in players:
        print(f'Ход пользователя {player}')
        user_num = int(input('Введите число от 1 до 100 \n'))

        if user_num == random_num:
            is_winner = True
            winner_name = player
            break

        if user_num > random_num:
            print('Вы ввели число больше загаданного\n')
        else:
            print('Вы ввели число меньше загаданного\n')

else:
    print(f'Поздравляем! Победитель {winner_name}!!!')
