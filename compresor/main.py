from PIL import Image
import os


rutaActual = os.path.dirname(os.path.abspath(__file__))

for nombre in os.listdir(rutaActual):
    name, extension = os.path.splitext(rutaActual + nombre)
    if extension in ['.png', '.jpg', '.jpeg']:
        foto = Image.open(rutaActual + '\\' + nombre)
        foto = foto.convert('RGB')
        foto.save(rutaActual+'/compresor' + "compressed_" + nombre, optimize=True, quality=60)
        print(rutaActual)
        print('Proceso realizado!')