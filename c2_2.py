import array

symbols = '$1234你好'

t = tuple(ord(symbol) for symbol in symbols)
print(t)

a = array.array('I', (ord(symbol) for symbol in symbols))

print(a)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)