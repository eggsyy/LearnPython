# coding=utf-8
# L = [x * x for x in range(10)]                          # 列表生成式
# print L
#
# g = (x * x for x in range(10))                          # 生成器
# print g.next()
# print g.next()
# for n in g:
#     print n


def fib(m):
    n, a, b = 0, 0, 1
    while n < m:
        print b
        a, b = b, a + b
        n = n + 1


fib(6)


def fib(m):
    n, a, b = 0, 0, 1
    while n < m:
        yield b
        a, b = b, a + b
        n = n + 1


print fib(6)
for fn in fib(6):
    print fn


def odd():
    print 'step1'
    yield 1
    print 'step2'
    yield 2
    print 'step3'
    yield 3


o = odd()
print o.next()
o.next()
o.next()
