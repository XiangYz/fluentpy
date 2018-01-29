def f(a, b):
    a += b
    return a

t = (10, 20)
u = (30, 40)

print(f(t, u))
print(t, u)

#元组不支持assignment，但是可以+=
x = (1, 2, 3)
x += (4, 5)
print(x)