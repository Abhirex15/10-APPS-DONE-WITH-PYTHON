import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 4444

clientsocket.connect(('192.168.0.105', port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('utf-8'))