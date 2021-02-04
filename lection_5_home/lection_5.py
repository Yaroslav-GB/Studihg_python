#map
#example

g = map(lambda  x: x*x, [1, 2, 3, 4, 55])

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

#reduce
#example_1

from functools import reduce

r = reduce(lambda acc, x: acc*x, [1, 2, 55, 77])

print(r)

#example_2

reduce(reverse, "asdf") #должен быть итог: "fdsa"  reverse не работает чет

#partial

from functools import partial

def power(x, y):
    return x**y

square = partial(power, y = 2)

