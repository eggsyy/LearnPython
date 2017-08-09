# -*-coding:utf-8 -*-
# 定义默认参数


# def power(x):
#     return x * x
#
#
# print power(5)
#
#
# def power(x, n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
#
#
# print power(5, 2)
#
#
# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
#
#
# print power(5)
# print power(5, 2)
#
#
# def enroll(name, gender, age=6, city='Beijing'):
#     print 'name:', name
#     print 'gender:', gender
#     print 'age:', age
#     print 'city:', city
#
#
# enroll('Sarah', 'F')
# print enroll('Bob', 'M', 7)
# print enroll('Adam', 'M', city='Shanghai')
#
#
# def add_end(L=[]):
#     L.append('END')
#     return L
#
#
# print add_end([1, 2, 3])
# print add_end()
# print add_end()
#
#
# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L
#
#
# print add_end()
# print add_end()


# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# num = [1, 2, 3]
# print calc([1, 2, 3])
# print calc(num)
#
#
# def calc(*numbers):                    # 可变参数组装成tuple
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# num1 = (1, 2, 3)                      # tuple
# print calc(1, 2, 3)
# print calc(*num1)
#
# num = [1, 2, 3]                       # list
# c = calc(num[0], num[1], num[2])
# print c
# d = calc(*num)
# print d


# def person(name, age, **kw):  # 关键字参数组装成dict
#     print 'name:', name, 'age:', age, 'other:', kw
#
#
# person('Micheal', 30)
# person('Bob', 35, city='Beijing')
# person('Adam', 45, gender='M', job='Engineer')
# kw = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, city=kw['city'], job=kw['job'])
# person('Jack', 24, **kw)


# 参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

func(1, 2)
func(1, 2, c=3)
func(1, 2, 3, 'a')
func(1, 2, 3, 'a', 'b', x=99)

args = (1, 2, 3, 4,)
kw = {'x': 99}
func(*args, **kw)
