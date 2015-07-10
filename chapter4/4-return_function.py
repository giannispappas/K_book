import math

def printLogarithm(x):
	if x<=0:
		print("Positive numbers only, please.")
		return
	result=math.log(x)
	print("The log of x is", result)
	
printLogarithm(-2)
printLogarithm(2)
