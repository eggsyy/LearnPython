import functools

print int('123456')
print int('123456', base=8)
print int('123456', 16)


def int2(x, base=2):
    return int(x, base)
print int2('100000')
print int2('10010100')


int22 = functools.partial(int, base=2)
print int22('100000')
print int22('1010101')

print int2('100000', base=10)
print int22('100000', base=10)

max2 = functools.partial(max, 10)
max3 = functools.partial(max)
print max2(5, 6, 7)
print max3(5, 6, 7)
