def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
print fact(1)
print fact(5)


def fact(n):
    return fact_iter(n, 1)


def fact_iter(n, total):                    # 尾递归
    if n == 1:
        return total
    return fact_iter(n-1, n * total)
print fact_iter(5, 1)
