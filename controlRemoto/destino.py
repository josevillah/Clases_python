import socket
import pyautogui

# Configuración del servidor
# Ip caja 1 Camilo Henriquez
host = '10.10.11.108'
port = 49667

# Crear un socket
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_socket.bind((host, port))
servidor_socket.listen(1)

# Aceptar una conexión entrante
cliente_socket, cliente_direccion = servidor_socket.accept()
print('Conexión establecida desde:', cliente_direccion)

# Bucle principal para recibir y ejecutar comandos remotos
while True:
    comando = cliente_socket.recv(1024).decode()

    if comando == 'capturar_pantalla':
        # Capturar pantalla y enviar imagen al cliente
        imagen = pyautogui.screenshot()
        imagen_bytes = imagen.tobytes()
        cliente_socket.sendall(imagen_bytes)

    elif comando == 'terminar_conexion':
        # Finalizar la conexión con el cliente
        break

# Cerrar los sockets
cliente_socket.close()
servidor_socket.close()
