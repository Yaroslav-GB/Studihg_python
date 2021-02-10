class Iter:
    def __init__(self, iterable_object):
        self.iterable_object = iterable_object
        self.index = 0

    def __next__(self):
        if self.index < len(self.iterable_object):
            result = self.iterable_object[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


class A:
    def __init__(self, xxx):
        self.xxx = xxx

    def __iter__(self):
        return Iter(self.__dict__.keys())


x = A([1, 2, 3, 4, 5])
x.yyy = 234
x.d = 555

for value in x:
    print(value)
