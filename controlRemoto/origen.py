import socket
import tkinter as tk
from PIL import ImageTk, Image


def get_local_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

local_ip = get_local_ip()
print("Dirección IP local:", local_ip)

# Configuración del cliente
host = local_ip
port = 49667

# Crear una ventana Tkinter
ventana = tk.Tk()

# Crear un lienzo para mostrar la pantalla remota
lienzo = tk.Canvas(ventana, width=800, height=600)
lienzo.pack()

# Función para actualizar la pantalla remota
def actualizar_pantalla():
    # Conectar al servidor
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect((host, port))

    # Enviar comando para capturar pantalla
    cliente_socket.sendall('capturar_pantalla'.encode())

    # Recibir imagen de la pantalla remota
    imagen_bytes = b''
    while True:
        datos = cliente_socket.recv(1024)
        if not datos:
            break
        imagen_bytes += datos

    # Mostrar la imagen en el lienzo
    imagen = ImageTk.PhotoImage(Image.frombytes('RGB', (800, 600), imagen_bytes))
    lienzo.create_image(0, 0, image=imagen, anchor=tk.NW)
    lienzo.image = imagen

    # Cerrar el socket
    cliente_socket.close()

    # Actualizar la pantalla cada cierto tiempo (en milisegundos)
    ventana.after(1000, actualizar_pantalla)

# Iniciar la actualización de la pantalla
actualizar_pantalla()

# Ejecutar el bucle principal de la ventana Tkinter
ventana.mainloop()
