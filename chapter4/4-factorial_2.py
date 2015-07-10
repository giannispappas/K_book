def factorial(n):
	if not isinstance(n, int):
		print('Το παραγοντικό ορίζεται μόνο για ακεραίους.')
		return -1
	elif n<0:
		print('Το παραγοντικό ορίζεται μόνο για θετικούς ακεραίους.')
		return- 1
	elif n == 0:
		return 1
	else:
		return n*factorial(n-1)

