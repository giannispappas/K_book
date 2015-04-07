import threading
import time
from collections import deque

lock = threading.Lock()
cond = threading.Condition(lock)

queue = deque(["1", "2", "3"])

def producer():
	while True:
		cond.acquire()
		# produce here
		s = "something"
		queue.append(s)
		print "produced %s" % s
		cond.notify() # or notifyAll to wake everyone up
		cond.release()
		time.sleep(1)

def consumer():
	while True:
		cond.acquire()
		# consume here
		s = queue.popleft()
		print "consumed %s" % s
		cond.wait() # sleep until item becomes available
		cond.release()
		time.sleep(1)

def thread1(p):
	print "Thread %s started" % threading.current_thread().name
	producer()

def thread2(p):
	print "Thread %s started" % threading.current_thread().name
	consumer()

def main():
	t1 = threading.Thread(target=thread1, name="T1", args=(0,))
	t1.start()
	t2 = threading.Thread(target=thread2, name="T2", args=(0,))
	t2.start()
	t1.join()
	t2.join()

if __name__ == '__main__':
	main()
