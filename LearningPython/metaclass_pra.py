from hello import Hello
h = Hello()
h.hello()
print type(Hello)
print type(h)


def fn(self, name='world'):
    print ('Hello, %s' % name)

Helloo = type('Hello', (object,), dict(hello=fn))
h = Helloo()
h.hello()
print type(h)


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list):
    __metaclass__ = ListMetaclass

L = MyList()
L.add(1)
L.add(2)
print L
