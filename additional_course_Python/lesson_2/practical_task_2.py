player_name = input('Enter player name ')
enemy_name = input('Enter enemy name ')
player = {
    'name': player_name,
    'health': 100,
    'damage': 50,
    'armor': 1.2
}

enemy = {
    'name': enemy_name,
    'health': 100,
    'damage': 45,
    'armor': 1.3
}


def attack(player1, player2):
    player1['health'] -= player2['damage'] // player1['armor']


attack(player, enemy)
attack(enemy, player)
print(f'{player_name} was attacked by {enemy_name}.\nResult: {player}')
print(f'{enemy_name} was attacked by {player_name}.\nResult: {enemy}')
