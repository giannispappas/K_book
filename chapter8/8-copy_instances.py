import copy

p1 = Point()
p1.x = 3.0
p1.y = 4.0
p2 = copy.copy(p1)
print(p1 == p2)
print(samePoint(p1,p2))