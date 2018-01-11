import time
import functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked


def clock2(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
        print(result)
    return clocked


@clock2
def snooze(seconds):
    """snooze sleep"""
    time.sleep(seconds)

@clock
def fact(n):
    '''factorial'''
    return 1 if n < 2 else n*fact(n-1)

@clock
@functools.lru_cache()
def fabonacci(n):
    return 1 if n <= 2 else fabonacci(n - 1) + fabonacci(n - 2)

if __name__ == '__main__':
    print('*' * 40, 'Calling snnoze(.123)')
    snooze(.123)
    print(snooze.__doc__)
    print('*' * 40, 'Calling fact(6)')
    print('6! = ', fact(6))
    print(fact.__doc__)

    print(fabonacci(200))