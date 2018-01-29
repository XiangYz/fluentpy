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

#装饰器后面跟括号表示需要调用一次这个函数才能得到真正的装饰器
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