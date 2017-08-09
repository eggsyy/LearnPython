
d = {'Eggsy': 100, 'Scotfield': 89, 'Scott': 98, 'Ronaldo': 100}
d['Eggsy'] = 88
print d['Eggsy']
print d.get('Scotfield')
print d.get('Sc', -1)
print d.get('sdf')
d.pop('Scotfield')
print d

# set
s = {1, 2, 2, 2, 3, 3, 3, 3}
s.add(4)
s.add(3)
s.remove(1)
s2 = {1, 2, 3, 5}
print 's =', s
print 's2 =', s2
print s & s2
print s | s2
