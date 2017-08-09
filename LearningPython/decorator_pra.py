def now():
    print "Now it's the time"
f = now
f()
print now.__name__
print f.__name__


def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper


@log
def now():
    print 'WTF'
now()


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator


@log('Execute')
def now():
    print '2017-07-29'
now()
