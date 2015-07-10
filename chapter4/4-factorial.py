def factorial(n):
	if n == 0:
		return 1
	else:
		return n*factorial(n-1)

x=3
print x,'!=', factorial(x)
