#Megan Shea

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Socket successfully created')
port = 9500
server_address = ('', port)

s.bind(server_address)
print('Socket binded to %s' %(port))

s.listen(1)
print('Socket is listening')

while True:
    c, addr = s.accept()
    #print('Got connection from', addr)
    #message = 'Thank you for connecting'
    #print()
    #c.send(message.encode())
    
    greeting = 'Hi'
    farewell = 'Goodbye'

    client_message = c.recv(1024)
    updated_message = client_message.decode('utf-8')
    print(updated_message)

    if updated_message == 'Hello':
        c.send(greeting.encode())
    else:
        c.send(farewell.encode())
    
    c.close()
    