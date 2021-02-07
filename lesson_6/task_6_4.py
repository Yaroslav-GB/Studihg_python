"""

4. Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать
текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости
свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.

"""
class Car:

    def __init__(self, color, name, speed, is_police):
        self.color = color
        self.name = name
        self.is_police = is_police
        self.speed = speed



    def go(self):
        return print(f'{self.name}, цвет {self.color} тронулась.')

    def stop(self):
        return print(f'{self.name}, цвет {self.color} остановилась.')

    def turn(self, direction):
        return print(f'{self.name}, цвет {self.color} {direction}')

    def show_speed(self):
        return print(f'{self.name}, цвет {self.color} '
                         f'едет со скоростью {self.speed} км\ч')

    def police(self):
        return print(self.is_police)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превысил скорость! {self.speed}км/ч')
        else:
            print(f'{self.name} едет {self.speed}км/ч, в пределах допустимой скорости.')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превысил скорость! {self.speed}км/ч')
        else:
            print(f'{self.name} едет {self.speed}км/ч, в пределах допустимой скорости.')

tc = TownCar('желтый', 'Школьный автобус', 70, False)
sc = Car('красный', 'Ferrari', 170, False)
wc = WorkCar('черный', 'Камаз', 60, False)
pc = Car('бело-сниний', 'УАЗ', 160, True)

tc.go()
tc.stop()
tc.turn('Повернула направо')
tc.show_speed()
tc.police()

sc.go()
sc.stop()
sc.turn('Повернула направо')
sc.show_speed()
sc.police()

wc.go()
wc.stop()
wc.turn('Повернула налево')
wc.show_speed()
wc.police()

pc.go()
pc.stop()
pc.turn('Развернулась')
pc.show_speed()
pc.police()

#, SportCar, WorkCar, PoliceCar.

