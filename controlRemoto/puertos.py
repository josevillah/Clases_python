import socket

def escanear_puertos(ip, puertos):
    for puerto in puertos:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Establece un tiempo de espera para la conexión

        resultado = sock.connect_ex((ip, puerto))
        if resultado == 0:
            print(f"Puerto {puerto} abierto en {ip}")
        else:
            print(f"Puerto {puerto} cerrado en {ip}")

        sock.close()

# Ejemplo de uso
ip_destino = '10.10.11.108'  # Ingresa la dirección IP del equipo destino
puertos_a_escanear = [80, 443, 3389, 22, 65535, 49667]  # Ingresa la lista de puertos a escanear

escanear_puertos(ip_destino, puertos_a_escanear)