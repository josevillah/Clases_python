""""
Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" a
partir de la siguiente estructura de carpetas: "curso Pytnon/Dia 6/practicas_path.py"

segundo ejercicio:
Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a
partir de la siguiente estructura de carpetas:home(directorio base)/Curso Pytnon/Día 6/practicas_path.py
"""

from pathlib import Path

carp1 = "Curso Python"
carp2 = "Día 6"
carp3 = "practicas_path.py"

ruta = Path(carp1,carp2,carp3)

# Ejercicio nº2


from pathlib import Path

carp1 = "Curso Python"
carp2 = "Día 6"
carp3 = "practicas_path.py"

base = Path.home()

ruta = Path(base,carp1,carp2,carp3)
print(ruta)
