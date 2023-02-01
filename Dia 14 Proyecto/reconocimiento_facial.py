import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

ruta = 'Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])
 
print(nombres_empleados)

# Codificar las imagenes
def codificar(imagenes):
    # Crear una lista nueva codificada
    lista_codificada = []

    # Pasar las imagenes a RGB
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        # codificar
        codificado = fr.face_encodings(imagen)[0]
        lista_codificada.append(codificado)

    # Devolver la lista    
    return lista_codificada

# Registrar ingresos
def registrar_ingresos(persona):
    f = open('registro.csv', 'r+')
    lista_datos = f.readlines()
    nombre_registro = []
    for line in lista_datos:
        ingreso = line.split(',')
        nombre_registro.append(ingreso[0])
    
    if persona not in nombre_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona}, {string_ahora}')


lista_empleados_codificada = codificar(mis_imagenes)


# Tomar una imagen de camara web
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)


# Leer imagen de la camara web
exito, imagen = captura.read()


if not exito:
    print('No se ha podido tomar la Imagen')
else:
    # Reconocer una cara con la camara web
    cara_captura = fr.face_locations(imagen)

    # Codificar cara capturada
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)
    
    # Buscar coincidencias de empleados
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)

        indice_coincidencias = numpy.argmin(distancias)

        # Mostrar coincidencias
        if distancias[indice_coincidencias] > 0.6:
            print('No coincide con ninguno de los empleados')
        else:
            # Buscar el nombre del empleado encontrado
            nombre = nombres_empleados[indice_coincidencias]
            
            # Obtener la ubicacion de de las corrrdenadas de la cara
            y1, x2, y2, x1 = caraubic
            # Generar el cuadro en la cara
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0,255,0), 2)
            # rectangulo para nombre
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0,255,0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255),2)

            registrar_ingresos(nombre)

            # Mostrar la imagen recibida
            cv2.imshow('Imagen web', imagen)

            # Mantener abierta
            cv2.waitKey(0)
