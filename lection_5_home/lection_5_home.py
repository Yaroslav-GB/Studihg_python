#repeat
#example


from itertools import repeat

j = 1
for i in repeat({}, 10):
    i[j] = j
    j+=1
    print(i)

#islice
#example

from itertools import islice

a = [1, 2, 3, 4, 5, 6]

s = list(islice(a, 1, 4))
print(s)

#cycle

from itertools import cycle
from itertools import islice

a = [1, 2, 3, 4, 5, 6]
g = cycle(a)                      #бесконечный цикл

b = list(islice(g, 20))
print(b)


#chain позволяет соединить 2 генератора
#example
from itertools import cycle
from itertools import islice
from itertools import chain

b = list(islice(cycle(chain(range(5), range(5, 0, -1))), 40))
print(b)

c = list(chain("gakebl", [5, 1, 8, 3, 4, 7, 3, 1]))
print(c)

#filterfalse
#example

from itertools import cycle
from itertools import islice
from itertools import chain
from itertools import filterfalse

a = list(filterfalse(lambda x: x % 3, range(20)))
print(a)