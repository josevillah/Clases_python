""""
Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.

Recuerda importar Path del módulo pathlib, y utilizar el método home()
"""
from pathlib import Path

ruta_base = Path.home()
print(ruta_base)