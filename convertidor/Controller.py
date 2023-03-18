import os
from os import remove
from PIL import Image
import cv2 as cv
import shutil
import numpy as np
from pathlib import Path

class Controller:
    def __init__(self):
        self.ruta = __file__.replace('Controller.py', '')
        self.carpeta_raiz = Path(self.ruta, 'terminado')
        self.ruta_destino = Path(self.ruta)
        self.ruta_destino = Path(self.ruta_destino, 'terminado')


    def sendFile(self, file, opt):
        self.fileName = Path(file).stem
        self.fileExtention = Path(file).suffix
        if not Path(file).is_dir():
            return self.convertTo(file, opt, self.fileName, self.fileExtention)
        else:
            for root, dirs, files in os.walk(file):
                for f in files:
                    newFile = Path(root, f)
                    self.fileName = Path(newFile).stem
                    self.fileExtention = Path(newFile).suffix
                    if self.convertTo(newFile, opt, self.fileName, self.fileExtention):
                        continue
                    else:
                        return False
            return True
                        


    def convertTo(self, file, opt, fileName, fileExtention):
        try:
            if opt == 'jpg':
                archivo_nuevo = str(file).replace(fileExtention, '.JPEG')
            else:
                archivo_nuevo = str(file).replace(fileExtention, '.'+opt)
            im = Image.open(file).convert("RGB")
            im.save(archivo_nuevo, opt)
            verificar = Path(self.ruta_destino, fileName+'.'+opt)
            if not os.path.exists(verificar):
                shutil.move(archivo_nuevo, self.ruta_destino)
                return True
            else:
                remove(verificar)
                shutil.move(archivo_nuevo, self.ruta_destino)
                return True
        except:
            return False


    def deleteImages(self):
        for root, dirs, files in os.walk(self.carpeta_raiz):
            if len(files) > 0:
                for f in files:
                    remove(Path(root,f))
                return True
            else:
                return False


    # def convertFolderTo(self):
    #     for root, dirs, files in os.walk(self.carpeta_raiz):
    #         for file in files:
    #             if file.endswith(".jpg"):
    #                 archivo = os.path.join(root, file)
    #                 archivo_nuevo = archivo.replace('.jpg', '.webp')
    #                 # Convertirlos a WebP
    #                 im = Image.open(archivo).convert("RGB")
    #                 im.save(archivo_nuevo,"webp")
    #                 print(archivo_nuevo)
    #                 shutil.move(archivo_nuevo, self.ruta_destino)        
    #             elif file.endswith(".png"):
    #                 archivo = os.path.join(root, file)
    #                 archivo_nuevo = archivo.replace('.png', '.webp')
    #                 # Convertirlos a WebP
    #                 im = Image.open(archivo).convert("RGB")
    #                 im.save(archivo_nuevo,"webp")
    #                 print(archivo_nuevo)
    #                 shutil.move(archivo_nuevo, self.ruta_destino)     
    #             elif file.endswith(".jpeg"):
    #                 archivo = os.path.join(root, file)
    #                 archivo_nuevo = archivo.replace('.jpeg', '.webp')
    #                 # Convertirlos a WebP
    #                 im = Image.open(archivo).convert("RGB")
    #                 im.save(archivo_nuevo,"webp")
    #                 print(archivo_nuevo)
    #                 shutil.move(archivo_nuevo, self.ruta_destino)     
    #             elif file.endswith(".gif"):
    #                 archivo = os.path.join(root, file)
    #                 archivo_nuevo = archivo.replace('.gif', '.webp')
    #                 # Convertirlos a WebP
    #                 im = Image.open(archivo).convert("RGB")
    #                 im.save(archivo_nuevo,"webp")
    #                 print(archivo_nuevo)
    #                 shutil.move(archivo_nuevo, self.ruta_destino)
    #             elif file.endswith(".jfif"):
    #                 archivo = os.path.join(root, file)
    #                 archivo_nuevo = archivo.replace('.jfif', '.webp')
    #                 # Convertirlos a WebP
    #                 im = Image.open(archivo).convert("RGB")
    #                 im.save(archivo_nuevo,"webp")
    #                 print(archivo_nuevo)
    #                 shutil.move(archivo_nuevo, self.ruta_destino)    
    #     print("¡Trabajo terminado!")