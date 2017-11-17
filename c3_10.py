from dis import dis


s1 = set(['spam', 'spam', 'eggs'])
print(s1)

s2 = set(('spam', 'abc'))
print(s2)

print(s1 & s2)
print(s1 | s2)
print(s1 - s2)


print(dis('{1}'))
print(dis('set([1])'))