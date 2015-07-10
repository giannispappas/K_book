import math

def area(radius):
	return math.pi*radius**2
	
def distance(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	dsquared = dx**2 + dy**2
	result = math.sqrt(dsquared)
	return result

def circle_area(xc, yc, xp, yp):
	return area(distance(xc, yc, xp, yp))
	
	