# encoding:utf-8
# 定义函数、调用函数
import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')  # 异常处理
    if x >= 0:
        return x
    else:
        return -x


a = int(raw_input('Please input an integer:'))
print my_abs(a)


# 定义空函数
def nope():
    pass  # 作为占位符


def move(c, b, step, angle=0):
    nx = c + step * math.cos(angle)
    ny = b - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print x, y
r = move(100, 100, 60, math.pi / 6)
print r
