import registration_param


registry = set()

def register(active = True):
    def decorate(func):
        print('running register(active=%s)->decorate(%s)'
            % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate


@register(active = False)
def f1():
    print('running f1()')

#装饰器工厂函数需要作为函数调用，即使不传参数
@register()
def f2():
    print('running f2()')

def f3():
    print('running f3()')


if __name__ == '__main__':
    f1()
    f2()
    f3()