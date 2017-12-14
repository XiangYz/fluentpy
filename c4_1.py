s = '你好'
print(len(s))
b = s.encode('gbk') #貌似gbk, gb2312, gb18030是一样的
print(b)
print(len(b))
print(b.decode('gbk'))