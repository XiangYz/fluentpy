def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n - 1)

fact = factorial



#列表推导可以代替map
print(list(map(fact, range(6))))
print([fact(n) for n in range(6)])
print(list(map(fact, filter(lambda n: n % 2, range(6)))))
print([fact(n) for n in range(6) if n % 2])