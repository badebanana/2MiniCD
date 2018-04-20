"""
 Implements a simple socket server

"""

import socket
import threading


def handle_client(name, client_connection):
    """Handles a client connection."""

    while True:
        # Print message from client
        msg = client_connection.recv(1024).decode()
        print('Received:', msg)

        # Check for exit
        if msg == 'exit':
            msg = 'Goodbye %s!' % name
            client_connection.sendall(msg.encode())
            break

        # Broadcast message to clients
        msg = '(%s) %s' % (name, msg)
        for conn in connections:
            conn.sendall(msg.encode())

    # Close client connection
    print('Client disconnected...')
    client_connection.close()
    connections.remove(client_connection)

    # Inform other users
    msg = 'User has left the server: %s' % name
    for conn in connections:
        conn.sendall(msg.encode())


# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

# Connection list
connections = []

clientList = []

#Função que nos permite saber se um elementos existe na lista
def exists(name):
    for i in clientList:
        if name.lower() == i.lower():
            return True;

    return False;

def acceptUser():
    name = client_connection.recv(1024).decode().strip(" ")
    while True:
        if exists(name):
            client_connection.send("Muda isso".encode())
            name = client_connection.recv(1024).decode().strip(" ")
        else:
            clientList.append(name)
            msg = 'You are now connected, %s!' % name
            print('Actual Clients Room:',clientList)
            client_connection.sendall(msg.encode())
            break
    return name

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Accept username
    name = acceptUser()

    # Welcome user
    msg = 'User has entered the server: %s' % name
    for conn in connections:
        conn.sendall(msg.encode())

    # Add connection
    connections.append(client_connection)

    # Create thread
    thread = threading.Thread(target=handle_client, args=(name, client_connection))
    thread.start()

# Close socket
server_socket.close()
