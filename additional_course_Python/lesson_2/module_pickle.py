import pickle

person = {'name': 'Max', 'phone': [8888888, 9999999], 'age': 666}

with open('person.dat', 'wb') as f:
    pickle.dump(person, f)

print('OBJECT RECORDED')

with open('person.dat', 'rb') as f:
    person_is_load = pickle.load(f)

print(person_is_load)
