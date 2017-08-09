# coding=utf-8
import os

print range(1, 11)
L = []

for x in range(1, 11):
    L.append(x * x)
print L

l = [x * x for x in range(1, 11)]                   # 列表生成式
print l

s = [x * x for x in range(1, 11) if x % 2 == 0]
print s

S = [m + n for m in 'ABC' for n in 'XYZ']
print S

F = [d for d in os.listdir('.')]                    # 列出当前目录下的所有文件和目录名
print F

d = {'x': 'A', 'y': 'B', 'z': 'C'}
D = [k + '=' + v for k, v in d.iteritems()]
print D

LL = ['Hello', 'FFF', 'IBM', 'Apple']
ll = [s.lower() for s in LL]
print ll
