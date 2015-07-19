import copy

b1 = Rectangle()
b1.width = 100.0
b1.height = 200.0
b1.corner = Point()
b1.corner.x = 0.0
b1.corner.y = 0.0
b2 = copy.copy(b1)
print(b1 == b2)
print(b1.corner == b2.corner)