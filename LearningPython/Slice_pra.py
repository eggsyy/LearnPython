# coding=utf-8
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#
# S = [L[0], L[1], L[2]]
# print S
#
# S = []
# n = 3
# for i in range(n):
#     S.append(L[i])
# print S
#
# S = L[0:3]                          # 从索引0开始，直到索引3为止，不包括3
# S1 = L[:3]
# S2 = L[1:3]
# S3 = L[-2:]
# S4 = L[-2:-1]
# print S
# print S1
# print S2
# print S3
# print S4

L = range(100)
print L[:10]
print L[-10:]
print L[10:20]
print L[:10:2]
print L[::5]
print (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)[::3]
print 'ABCDEFGH'[:3]
print 'ABCDEFGH'[::2]
