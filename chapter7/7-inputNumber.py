def inputNumber():
	x = int(input ('Pick a number:'))
	if x ==17:
		raise ValueError('17 is a bad number')
	print(x)

inputNumber()
	
