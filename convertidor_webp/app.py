import os
from PIL import Image
import cv2 as cv
import shutil
import numpy as np

# print('__file__:    ', __file__)

ruta = __file__.replace('app.py', '')
carpeta_raiz = ruta+"\images\\"
ruta_destino = ruta+"\\terminado\\"

# Localizar los archivos jpg
def convertir_webp():
    for root, dirs, files in os.walk(carpeta_raiz):
        for file in files:
            if file.endswith(".jpg"):
                archivo = os.path.join(root, file)
                archivo_nuevo = archivo.replace('.jpg', '.webp')
                # Convertirlos a WebP
                im = Image.open(archivo).convert("RGB")
                im.save(archivo_nuevo,"webp")
                print(archivo_nuevo)
                shutil.move(archivo_nuevo, ruta_destino)        
            elif file.endswith(".png"):
                archivo = os.path.join(root, file)
                archivo_nuevo = archivo.replace('.png', '.webp')
                # Convertirlos a WebP
                im = Image.open(archivo).convert("RGB")
                im.save(archivo_nuevo,"webp")
                print(archivo_nuevo)
                shutil.move(archivo_nuevo, ruta_destino)     
            elif file.endswith(".jpeg"):
                archivo = os.path.join(root, file)
                archivo_nuevo = archivo.replace('.jpeg', '.webp')
                # Convertirlos a WebP
                im = Image.open(archivo).convert("RGB")
                im.save(archivo_nuevo,"webp")
                print(archivo_nuevo)
                shutil.move(archivo_nuevo, ruta_destino)     
            elif file.endswith(".gif"):
                archivo = os.path.join(root, file)
                archivo_nuevo = archivo.replace('.gif', '.webp')
                # Convertirlos a WebP
                im = Image.open(archivo).convert("RGB")
                im.save(archivo_nuevo,"webp")
                print(archivo_nuevo)
                shutil.move(archivo_nuevo, ruta_destino)     
    print("¡Trabajo terminado!")


def convertir_jpg():
    for root, dirs, files in os.walk(carpeta_raiz):
        for file in files:      
            if file.endswith(".gif"):
                archivo = os.path.join(root, file)
                archivo_nuevo = archivo.replace('.gif', '.jpg')
                # Convertirlos a WebP
                im = Image.open(archivo).convert("RGB")
                im.save(archivo_nuevo,"JPEG")
                print(archivo_nuevo)
                shutil.move(archivo_nuevo, ruta_destino)     
            # elif file.endswith(".png"):
            #     archivo = os.path.join(root, file)
            #     archivo_nuevo = archivo.replace('.png', '.jpg')
            #     # Convertirlos a WebP
            #     im = Image.open(archivo).convert("RGB")
            #     im.save(archivo_nuevo,"JPEG")
            #     print(archivo_nuevo)
            #     shutil.move(archivo_nuevo, ruta_destino)     
    print("¡Trabajo terminado!")

convertir_webp()