""""
Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro,
y devuelva su contenido (read).
"""


def abrir_leer(ruta_archivo):
    archivo = open(ruta_archivo, "r")
    return archivo.read()


ruta = "registro.txt"
"""datos_archivo = abrir_leer(ruta)
print(datos_archivo)"""

"""
Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, 
y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"
"""

def sobrescribir(nombre_archivo):
    archivo = open(nombre_archivo, "w")
    archivo.write("contenido eliminado")


"""
Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, 
y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". 
Finalmente, debe cerrar el archivo abierto.
"se ha registrado un error de ejecución"
"""

def registro_error(nombre_archivo):
    archivo = open(nombre_archivo, "a")
    archivo.write("se ha registrado un error de ejecución")
    archivo.close()


