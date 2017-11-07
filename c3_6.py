import collections

class mydict(dict):
    
    def __missing__(self, key):
        print('no such key: ' + key)

    def __getitem__(self, key):
        return 'constant value'


d = mydict(hello = 1, hi = 2)
print(d)
print(d['hello'])        
print(d['ccc'])
print(d.get('hello'))