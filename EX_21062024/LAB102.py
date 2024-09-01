D = {'a': 10, 'b': 20, 'd': 30, 'c': 40, 'f': 12, 'e': 34}
print(D)

for k,v in D.items():
    print(k,v)

from collections import OrderedDict
d = OrderedDict()
d['a'] = 10
d['b'] = 20
d['d'] = 30
d['c'] = 40
d['f'] = 12
d['e'] = 34
print(d)