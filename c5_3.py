from functools import reduce
from operator import add


def myfunc(x, y):
    return x + y
        


s = reduce(myfunc, range(100))
print(s)
print(sum(range(100)))
print(dir(myfunc))