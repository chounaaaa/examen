import socket

HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

username = input("ingresar usuario: ")
client_socket.send(username.encode())

while True:
    comando = input("ingresar un comando (/adios para despedirse y /personajes pa ver los personajes): ")
    client_socket.send(comando.encode())

    if comando == "/adios":
        response = client_socket.recv(1024).decode()
        print(response)
        client_socket.close()
        break
    else:
        response = client_socket.recv(1024).decode()
        print(response)
