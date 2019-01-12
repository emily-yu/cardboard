# load additional Python module
import socket
from pymouse import PyMouse
from pykeyboard import PyKeyboard

# create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# retrieve local hostname
local_hostname = socket.gethostname()

# get fully qualified hostname
local_fqdn = socket.getfqdn()

# get the according IP address
ip_address = socket.gethostbyname(local_hostname)

# output hostname, domain name and IP address
print ("working on %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))

# bind the socket to the port 23456
server_address = (ip_address, 23456)  
print ('starting up on %s port %s' % server_address)  
sock.bind(server_address)

# listen for incoming connections (server mode) with one connection at a time
sock.listen(1)

width = None
height = None

while True:  
	# wait for a connection
	# print ('waiting for a connection')
	connection, client_address = sock.accept()

	try:
		# show who connected to us
		print ('connection from', client_address)

		# receive the data in small chunks and print it
		while True:
			data = connection.recv(64)
			if width is None:
				# output received data
				print ("width: %s" % data)
				width = float(data)
			elif height is None:
				print("height: %s" % data)
				height = float(data)
			else:
				# no more data -- quit the loop
				print ("no more data.")
				break

	finally:
		# Clean up the connection
		# print(width)
		# print(height)

		m = PyMouse()
		k = PyKeyboard()
		x_dim, y_dim = m.screen_size()

		m.click(x_dim * width, y_dim * height, 1)
		# print('done')

		connection.close()