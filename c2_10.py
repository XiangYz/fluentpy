import dis

s = ['a', 'b', 'c']
s1 = [s] * 3
print(s1)
s1[0][0] = 'A'
print(s1)


l = [1, 2, 3]
print(hex(id(l)))
l += [4, 5]
l *= 2
print(hex(id(l)))


print(dis.dis('s[a] += b'))