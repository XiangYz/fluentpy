import array


b1 = bytes('你好', encoding='utf_8')
print(b1)
print(hex(b1[0])) #是一个数
print(b1[:1]) #是同类型的bytes序列

print(b1[:1] == b1[0])
print('str'[:1] == 'str'[0])

print('你好'.encode('utf_8'))


b1_arr = bytearray(b1)
print(b1_arr)
print(b1_arr[-1:])

b2_arr = bytearray.fromhex('01 02 03 04')
print(b2_arr)


b2 = bytes.fromhex('e7 85 d5 32') #16进制字符串化为二进制数据的方法
print(b2)

numbers = array.array('b', [-2, -1, 0, 1, 2])
print(numbers)
octets = bytes(numbers)
print(octets)

b4 = array.array('I', [1, 2, 3, 4, 4294967295])
print(b4)
b4_bytes = bytes(b4)
print(b4_bytes)