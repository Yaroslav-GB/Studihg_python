class A:
    name = []

    def __init__(self, title):
        self.title = title

    def change_name(self, value):
        self.name = value

    @classmethod
    def get_A(cls, value):
        if value == 'CAR':
            return A('RED')
        else:
            return A('YELLOW')

    @staticmethod
    def do_something(value):
        print('do_something', value)


a = A.get_A('CARS')

a.change_name('CAR')
A.do_something('CAR')
print(a.title)
