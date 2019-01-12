# load additional Python module
import socket

import websockets
import asyncio
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import json
import time

# create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# retrieve local hostname
local_hostname = socket.gethostname()

# get fully qualified hostname
local_fqdn = socket.getfqdn()

# get the according IP address
# ip_address = socket.gethostbyname(local_hostname)
ip_address = socket.gethostbyname("127.0.0.1")

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


async def hello(websocket, path):
    coords = await websocket.recv()
    print(f"< {coords}")
    dimension = coords[1:-1].split(',')
    print(dimension)
    m = PyMouse()
    k = PyKeyboard()
    x_dim, y_dim = m.screen_size()

    m.click(x_dim * float(dimension[0]), y_dim * float(dimension[1]))

start_server = websockets.serve(hello, '169.231.167.2', 23456)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


# while True:  
#   # wait for a connection
#   # print ('waiting for a connection')

#   # try:
#       # show who connected to us
#   print('Ready to accept now...') 
#   connection, client_address = sock.accept()
#   print ('connection from', client_address)
#   # receive the data in small chunks and print it
#   time.sleep(1)
#   print ("1")

#   # data = connection.recv(4096)
#   # if (data != type(byte)):
#   while 1:
#       data = connection.recv(8000)
#       if not data: break
#       print(data)
#   # print (data)
#   # except:
#       # print ("REEEEEEEE")

#       # print (data.decode('utf-8'))
#       # if width is None:
#       #   # output received data
#       #   print ("width: %s" % data)
#       #   width = float(data)
#       # elif height is None:
#       #   print("height: %s" % data)
#       #   height = float(data.decode())
#       # else:
#       #   # no more data -- quit the loop
#       #   print ("no more data.")
#       #   break

#   # finally:
#       # Clean up the connection
#       # print(width)
#       # print(height)

#       # m = PyMouse()
#       # k = PyKeyboard()
#       # x_dim, y_dim = m.screen_size()

#       # m.click(x_dim * width, y_dim * height, 1)
#       # # print('done')

#       # connection.close()
# socket.close()