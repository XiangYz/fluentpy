from functools import reduce
from operator import add


def mygen():
    return x * y
        


s = reduce(myfunc, range(100))
print(s)
print(sum(range(100)))