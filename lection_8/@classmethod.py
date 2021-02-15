class A:
    name = []

    def __init__(self):
        self.title = 'by INIT'

    # def change_name(self, value):
    #    self.name = value

    @classmethod
    def change_name(cls, value):
        cls.name.append(value)
        cls.title = 'by CLS'


a = A()
print(a.name, a.title)

a.change_name('new name')
print(a.name, a.title)
