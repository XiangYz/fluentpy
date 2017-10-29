import array

symbols = '$1234你好'

t = tuple(ord(symbol) for symbol in symbols)
print(t)

a = array.array('I', (ord(symbol) for symbol in symbols))

print(a)