#First importing socket "Socket programming is a way of connecting two nodes on a network to communicate with each other."
import socket

#next create a socket object
s = socket.socket()
print("Socket created successfully ")

# reserve a port number
port = 12345

#Socket binding is process of binding a socket to a network address within the system. 
s.bind(('192.168.0.105',port))
print("socket binded to %s" %(port))

#put the socket into listening mode
s.listen(5)
print("socket is now listening")

#a forever loop untill we exit
#or an error occurs

while True:
	#Established connection with client
	c, addr = s.accept()
	print("Got connection from",addr)