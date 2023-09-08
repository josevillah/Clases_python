import socket

def solicitar_acceso(ip, puerto):
    mensaje = "Solicitud de acceso remoto"  # Puedes personalizar el mensaje de solicitud

    # Crear un socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conectar al equipo destino
        sock.connect((ip, puerto))
        print("Conexión establecida con éxito.")

        # Enviar la solicitud de acceso
        sock.sendall(mensaje.encode())
        print("Solicitud de acceso enviada.")

        # Esperar la respuesta del equipo destino
        respuesta = sock.recv(1024)
        print("Respuesta recibida:", respuesta.decode())

    except Exception as e:
        print("Error al conectar o enviar la solicitud:", str(e))

    finally:
        # Cerrar la conexión
        sock.close()
        print("Conexión cerrada.")

# Ejemplo de uso
ip_destino = '10.10.11.108'  # Ingresa la dirección IP del equipo destino
puerto_destino = 49667  # Ingresa el puerto que esté escuchando en el equipo destino

solicitar_acceso(ip_destino, puerto_destino)
