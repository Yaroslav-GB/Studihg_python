user_num = int(input('Введите число от 11 до 100: '))

while user_num > 10:
    user_num = int(input('Вы ввели не правильное число, '
                         'введите число от 11 до 100: '))
else:
    print(f'Ваше число во второй степени: {user_num ** 2}')
