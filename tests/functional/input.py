"""This file contains all supported python constructions.

Expected output:

1 2 3 4
val 10
0 1 2 3 4 5 6 7 8 9 10 0 1 2 3 4 5 6 7 8 9 10
items [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x 10
2
1
10
11
works
101 102

"""

from contextlib import contextmanager
from pathlib import Path
from shlex import quote


@contextmanager
def four():
    yield 4


with four() as f:
    xs = range(f)
    print(*map(lambda x: x + 1, xs))


def returning_range(x: int):
    yield from range(x)
    return x


def x_printer(x):
    val: int
    val = yield from returning_range(x)
    print(f'val {val}')


def formatter(x: int) -> dict:
    items: list = [*x_printer(x), x]
    print(*items, *items)
    return {'items': items}


result = {'x': 10, **formatter(10)}
for key, value in sorted(result.items(), key=lambda x: x[0]):
    print(key, value)

i = 2
while i:
    try:
        print(i)
    except Exception as e:
        print(e)
    finally:
        i -= 1


class NumberManager(metaclass=type):
    def ten(self):
        return 10

    @classmethod
    def eleven(cls):
        return 11


class ImportantNumberManager(NumberManager, metaclass=type):
    def ten(self):
        return super().ten()

    @classmethod
    def eleven(cls):
        return super().eleven()


class VeryImportantNumberManager(ImportantNumberManager):
    pass


print(ImportantNumberManager().ten())
print(VeryImportantNumberManager.eleven())

r = 'works' if True else 'fails'
print(r)
m = [x + 1 for x in range(100, 102)]
print(*m)
