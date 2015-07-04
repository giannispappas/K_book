def exists(filename):
	try:
		f = open(filename, 'r')
		f.close()
		return True
	except IOError:
		return False 