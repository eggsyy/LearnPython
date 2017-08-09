print sorted([345, 23, 5, 123, 4334, 0])


def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted([345, 23, 5, 123, 4334, 0], reversed_cmp)
print sorted([345, 23, 5, 123, 4334, 0][::-1])


def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob', 'about', 'Zeus', 'Credit'], cmp_ignore_case)
