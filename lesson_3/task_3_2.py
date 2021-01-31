"""

2. Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать в
ывод данных о пользователе одной строкой.


"""

def listDataUser (Name, Surname, Date, City, Mail, Phone):
    return '; '.join(["Имя: " + userName,
                      "Фамилия: " + userSurname,
                      "Год рождения: " + userDate,
                      "Город проживания: " + userCity,
                      "Почта: " + userMail,
                      "Номер телефона: " + userPhone]
                     )


userName = input("Введите имя ")
userSurname = input("Введите фамилию ")
userDate = input("Введите год рождения ")
userCity = input("Введите город проживания ")
userMail = input("Введите email ")
userPhone = input("Введите телефон ")

print(listDataUser(userName, userSurname, userDate, userCity, userMail, userPhone))

