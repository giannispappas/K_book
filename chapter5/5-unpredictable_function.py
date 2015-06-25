def unpredictable_function(n):
	while n!=1:
	 print(n)
	 if n%2 == 0: #n άρτιος
	  n=n//2
	 else:        #n περιττός
	  n=n*3+1
	 
unpredictable_function(6)
