#Megan Shea

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = '127.0.0.1'
port = 9500

s.connect((server, port))

message = 'Hello'
#print('This has connected')
s.send(message.encode())


server_message = s.recv(1024)
updated_message = server_message.decode('utf-8')
print(updated_message)


s.close()


