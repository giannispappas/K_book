t1 = ['a','b']
t2 = ['c','d','e']
t1.extend(t2)
print(t1)
letter = t1.pop(0)
print(letter)
print(t1)
t1.remove('e')
print(t1)