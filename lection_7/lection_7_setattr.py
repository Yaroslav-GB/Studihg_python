class A:
    def __init__(self, a):
        pass

    def __str__(self):
        return f'!{self.a}!'

    def __setattr__(self, key, value):
        if key == 'ddd':
            raise Exception('Вы не можете менять название')
        else:
            self.__dict__[key] = value


x = A(2)
x.ddd = 333
print(x.ddd)
