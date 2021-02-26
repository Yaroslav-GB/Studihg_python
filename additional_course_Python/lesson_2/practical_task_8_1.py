def person_data():
    name, year, city = input("Введи имя, возраст, "
                             "и город проживания через пробел ").split(' ')
    return f'{name}, {year} лет, проживет в городе {city}'


print(person_data())
