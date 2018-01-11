from dis import dis


def f(a):
    global d
    global b
    d = 1
    print(a)
    
    print(b)
    b = 9
    if a > 1:
        global c
        c = 3
    print(c)


if __name__ == '__main__':
    b = 1
    f(3)
    print(d)
    print(c)
    print(dis(f))