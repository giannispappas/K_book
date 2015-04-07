import threading

def func(i):
	print "Hello world, thread %d" % i
	

t = threading.Thread(target=func, args=(0,))
t.start()