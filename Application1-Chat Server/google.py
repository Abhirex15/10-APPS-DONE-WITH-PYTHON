#lets connect to Google
import socket
import sys
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Socket successfully created")
except socket.error as err:
	print("Socket creation failed with an error %s" %(err))

#default port for the socket
port = 80

try:
	host_ip = socket.gethostbyname('www.yahoo.com')
except socket.gaierror:
	print("there was an error resolving the host")
	sys.exit()

#connecting to the server
s.connect((host_ip, port))

print("The socket has successfully connected to Google \ on port == %s" %(host_ip))
