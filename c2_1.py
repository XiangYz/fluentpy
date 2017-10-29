symbols = '$1234你好'

beyond_ascii = [ord(c) for c in symbols if ord(c) > 127]
print(beyond_ascii)

beyond_ascii2 = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii2)