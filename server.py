import socket
import threading

# Configuración del servidor
HOST = 'localhost'  # Escucha en todas las interfaces de red
PORT = 8080

# Crear un socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

# Lista para almacenar las conexiones de clientes
clients = []

# Función para manejar las conexiones de los clientes
def handle_client(client_socket):
    # Pedir al cliente su nombre
    client_socket.send("Por favor, introduce tu nombre: ".encode('utf-8'))
    client_name = client_socket.recv(1024).decode('utf-8')

    while True:
        try:
            # Recibir un mensaje del cliente
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            # Formatear el mensaje con el nombre del cliente
            formatted_message = f"{client_name}: {message}"

            # Transmitir el mensaje a todos los clientes conectados
            for client in clients:
                client.send(formatted_message.encode('utf-8'))
        except Exception as e:
            print(f"Error: {str(e)}")
            break

    # Cerrar la conexión del cliente
    clients.remove(client_socket)
    client_socket.close()

# Función principal para aceptar conexiones entrantes
def main():
    print(f"Servidor escuchando en {HOST}:{PORT}")

    while True:
        client_socket, _ = server_socket.accept()
        clients.append(client_socket)

        # Iniciar un hilo para manejar la conexión del cliente
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()
