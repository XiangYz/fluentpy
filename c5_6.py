#指定关键字参数，传入b必须使用关键字参数形式
def fun(a, *c, b = 1):
    return ''.join('%s %s %s\n' % (a, i, b) for i in c)

print(fun(1, 2, 3, 4))
print(fun(1, b = 2))