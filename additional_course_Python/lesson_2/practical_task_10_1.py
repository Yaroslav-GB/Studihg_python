import sys, os

name = 'dir_'


# print(name)
def to_create():
    for i in range(1, 10):
        new_path = os.path.join(os.getcwd(), f'{name}{i}')
        os.mkdir(new_path)


def to_delete():
    for i in range(1, 10):
        new_path = os.path.join(os.getcwd(), f'{name}{i}')
        os.rmdir(new_path)


to_create()
to_delete()
