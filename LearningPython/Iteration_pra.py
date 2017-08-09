# coding=utf-8
from collections import Iterable                # collections模块Iterable类型

d = {'a': 1, 'b': 2, 'c': 3}                    # 字典迭代
print d.items()
for key in d:
    print key
for value in d.itervalues():
    print value
for k, v in d.iteritems():
    print k, v

for ch in 'ABC':                                # 字符串迭代
    print ch

print isinstance('abc', Iterable)
print isinstance([1, 2, 3], Iterable)
print isinstance(123, Iterable)

for i, value in enumerate(['A', 'B', 'C']):
    print i, value
