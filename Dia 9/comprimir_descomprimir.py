import zipfile

archivo = zipfile.ZipFile('archivos.zip', 'w')
archivo.write('Muebles sistema.xls')