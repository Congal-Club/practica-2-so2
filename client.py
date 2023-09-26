import socket
import threading

# Configuración del cliente
HOST = 'localhost'  # Cambia esto para conectarte al servidor remoto
PORT = 8080

# Crear un socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Función para recibir mensajes del servidor
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except Exception as e:
            print(f"Error al recibir mensajes: {str(e)}")
            break

# Función principal para enviar mensajes al servidor
def send_messages():
    client_name = input("Introduce tu nombre: ")
    client_socket.send(client_name.encode('utf-8'))

    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

# Iniciar hilos para recibir y enviar mensajes
thread_recv = threading.Thread(target=receive_messages)
thread_send = threading.Thread(target=send_messages)

thread_recv.start()
thread_send.start()
