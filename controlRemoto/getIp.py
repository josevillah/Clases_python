import requests

def obtener_ip_publica():
    try:
        # Realizar una solicitud GET a la API de ipify
        response = requests.get('https://api.ipify.org?format=json')
        
        # Extraer la dirección IP de la respuesta JSON
        ip = response.json()['ip']
        
        return ip
    except requests.RequestException:
        # Manejar errores de conexión o solicitud
        print('No se pudo obtener la dirección IP pública.')
        return None

# Obtener y mostrar la dirección IP pública
ip_publica = obtener_ip_publica()
if ip_publica:
    print(f'La dirección IP pública es: {ip_publica}')
