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

#Função que pergunta qual o Username do utilizador
def requestUsername():
    print('$ Username?')
    name = input('> ')
    return name

#Função para registar o Utilizador
def registerUsername(name):
    client_socket.sendall(name.encode())
    res = client_socket.recv(1024).decode()

    while True:
        if res == "True":
            print("O nome " , name, " já está a ser usado. Tente outro nome.")
            name = requestUsername()
            client_socket.sendall(name.encode())
            res = client_socket.recv(1024).decode()
        else:
            break

    print('$', res)

def menu():
    print('\n1-Criar nova sala')
    print('2-Inscrever-se numa sala')
    option = input('> ')
    if option == '1' or option == '2':
        print('Nome da sala:')
        nameRoom = option
        nameRoom += input('> ')
        client_socket.sendall(nameRoom.encode())


# Define socket host and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Request username
name = requestUsername()

# Connect to server
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Register username
registerUsername(name)

#Menu
menu()

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
