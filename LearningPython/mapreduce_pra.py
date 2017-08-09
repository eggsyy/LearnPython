# def f(x):
#     return x * x
# print map(f, [1, 2, 3, 4, 5, 6, 7])
#
# print map(str, [1, 2, 3, 4, 5, 6])
#
# # reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#
#
# def add(x, y):
#     return x + y
# print reduce(add, [1, 2, 3, 4, 5])
#
#
# def fn(x, y):
#     return x * 10 + y
# print reduce(fn, [1, 3, 5, 7, 9])


# def fn(x, y):
#     return x * 10 + y
#
#
# def char2num(s):
#     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#
#
# print reduce(fn, map(char2num, '145678'))
#
#
# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#
#     def char2num(s):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#
#     return reduce(fn, map(char2num, '145678'))
# print str2int('145678')
#
#
# def char2num(s):
#     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#
#
# def str2int(s):
#     return reduce(lambda x, y: x * 10 + y, map(char2num, s))
# print str2int('145678')

def normal(s):
    return s[0].upper() + s[1:].lower()
fm = map(normal, ['adam', 'LISa', 'BarT'])
print fm


def prod(s):
    return reduce(lambda x, y: x * y, s)
f = prod([1, 2, 3, 4, 5])
print f
