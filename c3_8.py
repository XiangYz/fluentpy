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


d = StrKeyDict({'a':1, 234:2, '$':3})
print(d)
print(d['a'])
print(d.get(234))
#???????????
print(d.get('xc,mnv,xcn'))