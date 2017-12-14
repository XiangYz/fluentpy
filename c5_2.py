import array

def factorial(n):
    '''returns n!'''
    #return后面可以接if else表达式
    return 1 if n < 2 else n * factorial(n - 1)

fact = factorial



#列表推导可以代替map
print(tuple(map(fact, range(6))))
print(tuple(fact(n) for n in range(6)))
print(list(map(fact, filter(lambda n: n % 2, range(6)))))
print([fact(n) for n in range(6) if n % 2])
#生成器表达式是一个可迭代对象，可以初始化元组、列表、字节序列、数组、集合等
print(bytes(i for i in range(6)) )
arr = array.array('B', (i for i in range(70) if i >= 65))

for i in arr:
    print(i)