#encoding:utf-8
age = int(raw_input('Please enter your age:'))
print'Your age is',age
if age >= 18:
	print"You're an adult"
elif age >= 13:
	print"You're a teenager"
else:
	print"You're a kid"

names = ['Teddy','Eggsy','Micheal']
for name in names:
	print name

sum = 0
for x in[1,2,3,4,5,6,7,8,9,10]:
	sum = sum + x
print sum

sum = 0
for x in range(101):
	sum = sum + x
print sum

sum = 0
n = 100
while n > 0:
	sum = sum + n
	n = n - 1
print sum

birth = int(raw_input('Input your birthyear:'))
if birth < 2000:
	print u'You are a 00前'
else:
	print u'You are a 00后'