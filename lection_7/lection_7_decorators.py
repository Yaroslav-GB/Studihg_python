def prepend_dashes(func):
    def xxx(*args, **kwargs):
        print('----')
        result = func(*args, **kwargs)
        print('++++++')
        return result

    return xxx


@prepend_dashes
def move_to(place):
    print('move_to', place)


@prepend_dashes
def observe(sightseen):
    print('observe', sightseen)


@prepend_dashes
def eat(meal):
    print('eat', meal)


@prepend_dashes
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
    activity()
