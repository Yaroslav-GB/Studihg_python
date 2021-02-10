class CarBrokenError(Exception):
    pass


class SightIsNotAvailableError(Exception):
    pass


def move_to(place):
    raise CarBrokenError()
    print('move_to', place)


def observe(sightseen):
    print('observe', sightseen)


def eat(meal):
    print('eat', meal)


def rest():
    print('rest')


from functools import partial

activities = [
    partial(move_to, 'London'),
    partial(observe, 'Thamse'),
    partial(eat, 'Tea'),
    partial(rest, ),
    partial(move_to, 'Paris'),
    partial(observe, 'Eiffel'),
    partial(eat, 'croasson'),
    partial(rest, ),
    partial(move_to, 'home'),
    partial(observe, 'tv'),
    partial(eat, 'whatever you like'),
    partial(rest, ),
]
for activity in activities:
    try:
        activity()
    except SightIsNotAvailableError as e:
        print("Некуй тут делать!")
    except CarBrokenError as e:
        print("Тачка брокен! Бегим пешком!!")
    except Exception as e:
        print(e)
        exit(1)
