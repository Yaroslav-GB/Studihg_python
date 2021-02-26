user_name = input('Введите имя ')
user_surname = input('Введите фамилию ')
user_age = int(input('Введите возраст '))
user_weight = int(input('Введите вес '))

if user_age <= 30 and user_weight >= 50 and user_weight <= 120:
    print(f'{user_name}{user_surname}, {user_age} год, '
          f'вес {user_weight}кг - хорошее состояние')
elif user_age > 30 and user_age < 40:
    if user_weight < 50 or user_weight >= 120:
        print(f'{user_name}{user_surname}, {user_age} год, '
              f'вес {user_weight}кг - Пациенту требуется заняться собой')
elif user_age > 40 and (user_weight < 50 or user_weight) >= 120:
    print(f'{user_name}{user_surname}, {user_age} год, '
          f'вес {user_weight}кг - Пациенту требуется врачебный осмотр')
elif user_age > 30 and (user_weight >= 50 or user_weight <= 120):
    print(f'{user_name}{user_surname}, {user_age} год, '
          f'вес {user_weight}кг - хорошее состояние')



else:
    print('Вы труп')
