"""

********** caracteres especiales: **********
    car - descripcion - ejemplo
    /d - Digito numerico - v\d.\d\d
    /w - caracter alfanumerico - \w\w\w-\w\w
    /s - Especio en blanco - numero\s\d\d
    /D - No es numerico - \D\D\D\D
    /W - No es alfanumerico - \W\W\W
    /S - No es un espacio en blanco \S\S\S\S

"""

"""

********** caracteres Cuantificadores: **********
    car - descripcion - ejemplo
    +   - 1 o mas veces - codigo_\d\d+
    {n} - se repite n veces - \d-\d{4}
    {n,m} - se repide de n a m veces \w{3,5}
    {n,} - desde n hacia arriba -\d{4,}-
    *   - 0 o mas   -   \w\s*\w
    ?   - 1 o 0     -   casas?
"""

import re

texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

patron = 'ayuda'

busqueda = re.search(patron, texto)
print(busqueda)

# Cuantas veces se repiten
busqueda = re.findall(patron, texto)
print(busqueda)

for conseguir in re.finditer(patron, texto):
    print(conseguir.span())

numero = "llama al 564-525-6588 ya mismo!"
patron = r"\d{3}-\d{3}-\d{4}"

busqueda = re.search(patron, numero)
print(busqueda.group())

patron = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
busqueda = re.search(patron, numero)
print(busqueda.group(2))

# Crear una contraseña que siga un patron
"""clave = input("Ingrese contraseña: ")
patron = r"\D{1}\w{7}"
revisar = re.search(patron, clave)
print(revisar)
"""


def verificar_email(email):
    patron = r"\w{1,}@\w{1,}\Wcom"
    revisar = re.search(patron, email)
    if revisar:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")


# verificar_email("1994@gmail.com")


def verificar_saludo(frase):
    revisar = re.search(r'^Hola', frase)
    if revisar:
        print("Ok")
    else:
        print("No has saludado")


# verificar_saludo("Hola como estas?")


def verificar_cp(cp):
    patron = r"\w{2}\d{4}"
    verificar = re.search(patron, cp)
    if verificar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")


verificar_cp("xx1234")