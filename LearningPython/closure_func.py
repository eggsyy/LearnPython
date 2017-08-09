def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
print calc_sum(1, 2, 3, 4)


def lazy_sum(*args):
    def sum_1():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum_1
print lazy_sum(1, 2, 3, 4, 5)
f = lazy_sum(1, 2, 3, 4, 5)
print f()
f1 = lazy_sum(1, 2, 3, 4, 5)
print f == f1


def squ():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1, f2, f3 = squ()
print f1(), f2(), f3()


def squ1():
    fs = []
    for i in range(1, 4):
        def f(j = i):
            return j * j
        fs.append(f)
    return fs
f1, f2, f3 = squ1()
print f1(), f2(), f3()
