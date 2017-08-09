print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7])

f = lambda x: x * x
print f
print f(5)


def build(x, y):
    return lambda: x * x + y * y
f = build(1, 2)
print f()


def build_1():
    return lambda x, y: x * x + y * y
f = build_1()
print f(1, 2)
