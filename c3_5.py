import collections

class StrKeyDict(collections.UserDict):
    
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    # def get(self, key, default=None):
    #     try:
    #         return self[key]
    #     except KeyError:
    #         return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


d = StrKeyDict0({'a':1, 'b':2, 'c':3})
print(d)

print(d['a'])
print(d.get('a'))


#print(d['d'])
print(d.get('d'))
