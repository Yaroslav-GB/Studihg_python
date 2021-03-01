import json
import pickle

favourite_group = [
    {'name': 'Slayer', 'tracks': ['New Faith', 'Raining Blood', 'Bloodline'],
     'albums': [{'name': 'Diabolus In Musica', 'year': 1996}, {'name': 'God Hates Us All', 'year': 2001}]
     }
]

with open('group.json', 'w', encoding='utf-8') as fp:
    json.dump(favourite_group, fp)

print('JSON RECORDED')

with open('group.dat', 'wb') as f:
    pickle.dump(favourite_group, f)

print('PICKLE RECORDED')

with open('group.dat', 'rb') as f:
    group_P_is_load = pickle.load(f)

print(group_P_is_load)

with open('group.json', 'r') as f:
    group_J_is_load = json.load(f)

print(group_J_is_load)
