from functools import reduce
from operator import mul

def fact(n):
    return reduce(lambda a, b: a*b, range(1, n+1))

def fact2(n):
    res = 1
    while n >= 1:
        res *= n
        n -= 1
    return res

def fact3(n):
    return reduce(mul, range(1, n + 1))

print(fact(10))
print(fact2(10))
print(fact3(10))