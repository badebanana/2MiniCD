"""
 Implements a simple socket client

"""

import socket
import threading

def handle_messages(client_socket):
    """Handles all incoming messages."""

    while is_running:
        # Read answer
        res = client_socket.recv(1024).decode()
        print(res)

    # Close socket
    client_socket.close()

def requesteUsername():
    # Request username
    print('$ Username?')
    name = input("> ")
    return name

def userExists(res):
    if res == 'The user %s already exists' % name:
        print('$', res)
        newName = requesteUsername()
        client_socket.sendall(newName.encode())

    else:
        print('$', res)

# Define socket host and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

name = requesteUsername()

# Connect to server
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Register username
client_socket.sendall(name.encode())
res = client_socket.recv(1024).decode()
userExists(res)

# Start listening to messages
is_running = True
thread = threading.Thread(target=handle_messages, args=(client_socket, ))
thread.start()

while True:
    # Send message
    msg = input('')
    client_socket.sendall(msg.encode())

    # Check for exit
    if msg == 'exit':
        break

is_running = False
