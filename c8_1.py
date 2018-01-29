import time


alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
charles = alex
lewis = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}

print(id(alex))
print(id(charles))
print(id(lewis))

# is用来判断是否引用的同一个对象
print(alex is charles)
print(alex is lewis)
# == 用来判断值是否相等
print(alex == lewis)

l1 = [1, [2, 3], [4, 5, 6]]
l2 = list(l1)
l3 = l1[:]

l1[1].append(4)

print(l2)
print(l3)