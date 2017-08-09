class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__

    def __call__(self):
        print ('My name is %s' % self.name)

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda x: x + 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
print Student('Michael')
s = Student('Mike')
print s.score
print s.age(6)
# print s.grade
s()

# class Fib(object):
#     # def __init__(self):
#     #     self.a, self.b = 0, 1
#     #
#     # def __iter__(self):
#     #     return self
#     #
#     # def next(self):
#     #     self.a, self.b = self.b, self.a + self.b
#     #     if self.a > 100:
#     #         raise StopIteration()
#     #     return self.a
#
#     def __getitem__(self, n1):
#         if isinstance(n1, int):
#             a, b = 1, 1
#             for x in range(n1):
#                 a, b = b, a + b
#             return a
#         if isinstance(n1, slice):
#             start = n1.start
#             stop = n1.stop
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a + b
#             return L
#
# for n in Fib():
#     print n
#
# f = Fib()
# print f[0]
# print f[100]
# print f[0:5]
# print f[:10]

#
# class Chain(object):
#     def __init__(self, path = ''):
#         self._path = path
#
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
#
#     def __str__(self):
#         return self._path
#
# print Chain().status.user.Time.line.list

