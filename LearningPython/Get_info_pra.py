import types

print type(123)
print type('str')
print type(None)
print type(abs)
print type(123) == type(456)
print type('abc') == type(023)
print type('abd') == type('123')
print type('abc') == types.StringType
print type(u'abc') == types.UnicodeType
print type(int) == type(str) == types.TypeType
print dir('ABC')
print len('aBC')
print 'ABC'.__len__()


class MyObject(object):
    def __len__(self):
        return 100

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x
obj = MyObject()
print hasattr(obj, 'x')
print obj.x
print hasattr(obj, 'y')
setattr(obj, 'y', 19)
print hasattr(obj, 'y')
print getattr(obj, 'y')
print obj.y
print getattr(obj, 'y', 404)
print getattr(obj, 'z', 404)
print hasattr(obj, 'power')
print getattr(obj, 'power')
fn = getattr(obj, 'power')
print fn
print fn()
