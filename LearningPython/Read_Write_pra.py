# coding=utf-8
import codecs

try:
    f = open('C:/Users/user/Desktop/test.txt', 'r')
    print f.read()
    print type(f.read())
finally:
    if f:
        f.close()

with open('C:/Users/user/Desktop/1.txt', 'r') as f:
    print f.read().decode('gbk')

# f = open('C:/Users/user/Desktop/1.jpg', 'rb')
# print f.read()
with codecs.open('C:/Users/user/Desktop/1.txt', 'r', 'gbk') as f:
    print f.read()

f = open('C:/Users/user/Desktop/1.txt', 'w')
f.write('You handing')
f.close()

with open('C:/Users/user/Desktop/1.txt', 'w') as f:
    f.write('you idiot')

