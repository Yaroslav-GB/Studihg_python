def gen(x):
    for y in range(x+1):
        yield y*y

for i in gen(10):
    print(i)


g = gen(10)
print(g, type(g))