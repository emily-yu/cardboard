# load additional Python module
import socket
import websockets
import asyncio
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import pyscreenshot as ImageGrab
from PIL import Image
import base64
from io import BytesIO

# create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# retrieve local hostname
local_hostname = socket.gethostname()

# get fully qualified hostname
local_fqdn = socket.getfqdn()

# get the according IP address
# ip_address = socket.gethostbyname(local_hostname)
ip_address = socket.gethostbyname("127.0.0.1")

# output hostname, domain name and IP address - change to unique IP address
print ("working on %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))

# bind the socket to the port 23456
server_address = (ip_address, 23456)  
print ('starting up on %s port %s' % server_address)  
sock.bind(server_address)

# listen for incoming connections (server mode) with one connection at a time
sock.listen(3)
 
async def run_server(websocket, path):

	while True:

		coords = await websocket.recv()
		print(f"Received from client {coords}")
		if len(coords) > 1:
			dimension = coords[1:-1].split(',')
			m = PyMouse()
			x_dim, y_dim = m.screen_size()
			m.click(x_dim * float(dimension[0]), y_dim * float(dimension[1]))
		else:
			k = PyKeyboard()
			k.tap_key(String.fromCharCode(coords))

		img = ImageGrab.grab()
		img.save('screenshot.png')
		print(f'Took screenshot')
		time.sleep(1.5)
		# img.show()
		buffered = BytesIO()
		img.save(buffered, format="PNG")
		image_base64 = base64.b64encode(buffered.getvalue())

		await websocket.send(image_base64.decode('utf-8'))

		# await websocket.send('sending data back to client')
		
		payload = {"base64": image_base64.decode('utf-8')}
	# return payload

# start_server = websockets.serve(run_server, 'localhost', 8765)
start_server = websockets.serve(run_server, '10.30.3.126', 23456)
# websockets.serve(run_server, '10.30.3.126', 23456)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
