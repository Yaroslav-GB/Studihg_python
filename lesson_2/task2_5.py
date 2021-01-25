#5. Реализовать структуру «Рейтинг», представляющую собой не
# возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
myRating = [2, 5, 10, 6, 1, 9, 5, 7, 8]
myRating = sorted(myRating, reverse=True)
print(f"Начальный рейтинг: {myRating}")
userDigit = int(input("Введите натуральное число (для завершения введите '0') "))
while userDigit != 0:
    for el in range(len(myRating)):
        if userDigit == myRating[el]:
            myRating.insert(el + 1, userDigit)
            break
        elif userDigit > myRating[el]:
            myRating.insert(el, userDigit)
            break
        elif userDigit < myRating[el]:
            myRating.insert(el - 1, userDigit)
            break
    myRating = sorted(myRating, reverse=True)
    print(f"Текущий рейтинг: {myRating}")
    userDigit = int(input("Введите натуральное число (для завершения введите '0') "))
