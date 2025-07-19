import socket
import requests

HOST = '127.2.2.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Servidor escuchando en el puerto", PORT)

while True:
    client_socket, address = server_socket.accept()
    print("Conexión establecida con", address)

    username = client_socket.recv(1024).decode()
    print("Nombre de usuario:", username)

    while True:
        comando = client_socket.recv(1024).decode()
        print("Comando recibido:", comando)

        if comando == "/episodios":
            response = requests.get("https://rickandmortyapi.com/api/episode")
            data = response.json()
            cantidad_episodios = data["info"]["count"]
            mensaje = f"La cantidad total de episodios es: {cantidad_episodios}"
            client_socket.send(mensaje.encode())

        elif comando == "/adios":
            client_socket.send("Chau bro".encode())
            client_socket.close()
            print("Conexión cerrada")
            break
