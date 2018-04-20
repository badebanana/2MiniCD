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

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Accept username
    name = client_connection.recv(1024).decode()
    msg = 'You are now connected, %s!' % name
    client_connection.sendall(msg.encode())

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
