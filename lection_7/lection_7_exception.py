class MeException(Exception):
    pass


def f():
    raise MeException('Тут косяк')


try:
    a = f()
except Exception as e:
    print(e)
