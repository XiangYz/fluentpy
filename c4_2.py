import array


b1 = bytes('你好', encoding='utf_8')
print(b1)
print(hex(b1[0]))
print(b1[:1])

print(b1[:1] == b1[0])
print('str'[:1] == 'str'[0])

print('你好'.encode('utf_8'))


b1_arr = bytearray(b1)
print(b1_arr)
print(b1_arr[-1:])


b2 = bytes.fromhex('e7 85 d5 32')
print(b2)

numbers = array.array('b', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
print(octets)