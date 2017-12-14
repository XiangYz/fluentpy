from functools import reduce
from operator import add


def myfunc(x, y):
    return x + y
        


s = reduce(myfunc, range(1, 101))
print(s)
print(sum(range(1, 101)))

print(dir(myfunc))


sa = ['1234', '567', '89']
print(reduce(add, sa))

#可迭代序列都可以作为sum的参数
print(sum(n for n in range(1, 101) if n % 2 == 0))
print(sum((1, 2, 3, 4)))
print(sum([1, 2, 3, 4]))
print(sum({1, 2, 3, 4}))
