import time
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.168.11', 8888))
print "Connected to echo server"

echo = """Testing\n1\n2\n3"""

try:
	for line in echo.splitlines():
		sock.sendall(line)
		print "Sent:", line
		try:
			# Uncomment delay to crash client before receiving server response
			#time.sleep(5) # delay here
			response = sock.recv(1024)
		except socket.error as (value, message):
			# Server may reset connection (terminate
			# abnormally) while client waits to
			# receive next echo line. Print message,
			# then go up to send next line (if any)
			print "Socket error while waiting to receive: (value:", value, ") " + message
		except:
			print "Unexpected error"
			break
		print "Received:", response

		if not response: break
		
except:
	print "Unexpected error in echo loop"

sock.close()
