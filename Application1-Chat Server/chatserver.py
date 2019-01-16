import socket
import sys
import time

#CHAT SERVER

s = socket.socket()
host = socket.gethostname()
print("Server will start on host :", host)
port = 8080
s.bind((host, port))

print("")
print("Done Binding with the host..")
print("")

s.listen()
c, addr = s.accept()
print(addr, "Has connected to the server is now online.. ")
print("")
while 1:
    message = input(str(">>"))
    message = message.encode()
    c.send(message)
    print("Message has been sent!")
    print("")
    incoming_message = c.recv(1024)
    incoming_message = incoming_message.decode()
    print("Server: ",incoming_message)
    print("")
