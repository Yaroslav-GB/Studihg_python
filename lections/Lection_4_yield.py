

def fib():
    a = 1
    b = 0
    c = 0
    while True:
        c = b + a
        a = b
        b = c
        if c < 100:
            yield c
            #yield c
        else:
            break

for f in fib():
    print(f)


print(fib())
print(fib())
print(fib())
print(fib())
print(fib())
print(fib())



