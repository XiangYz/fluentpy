tt = (1, 2, (30, 40))
print(hash(tt))

tf = (1, 2, frozenset([30, 40]))
print(hash(tf))

# tl = (1, 2, [30, 40])
# print(hash(tl))


a = dict(one = 1, two = 2, three = 3)
b = {'one':1, 'two':2, 'three':3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three':3, 'one':1, 'two':2})

print(a)
print(b)
print(c)
print(d)
print(e)

print(a == b == c == d == e)