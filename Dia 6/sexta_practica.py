"""
1) Saludo de Bienvenida.
2) Informar la ruta donde se encunta el directorio de recetas.
3) informar cuantas recetas hay dentro de esa carpeta.
4) menu de opciones:

    opcion 1 - leer receta
        4.1.1)elegir categoria
        4.1.2)mostrar recetas
        4.1.3)debe elegir una receta
        4.1.4)leer receta

    opcion 2 - crear receta
        4.2.1)elegir categoria
        4.2.2)crear nombre
        4.2.3)crear contenido

    opcion 3 - crear categoria

    opcion 4 - eliminar receta
        4.4.1)elegir categoria
        4.4.2)mostrar recetas
        4.4.3)debe elegir una receta
        4.4.4)eliminar receta

    opcion 5 - Eliminar categoria
        4.5.1)elegir categoria

    opcion 6 - Finalizar sistema
        4.6.1) debe detener la ejecucion del codigo
"""

from pathlib import Path
from os import system
import os


def informar_ruta(url):
    archivos = Path(url)
    print(f"El recetario esta registrado en: {archivos.parent}")


def contar_recetarios_totales(url):
    recetas = []
    indice = 0
    for txt in Path(url).glob("**/*.txt"):
        recetas.append(txt)

    cantidad_recetas = len(recetas)
    return cantidad_recetas


def validar_datos(opcion):
    opcion_entero = 0
    validar_letas = "abcdefghijklmnñopqrstuvwxyz"
    validar_signos = "|°'¬!#$%&/()=?¡'¿\><´´*+~^^{}[]-_.:,;"
    if len(opcion) == 1:
        if validar_signos.find(opcion) < 0:
            if validar_letas.find(opcion) < 0:
                opcion_entero = int(opcion)
                if opcion_entero == 6:
                    print("Vuelve pronto!")
                    return opcion_entero
                else:
                    return opcion_entero
            else:
                print("solo debes ingresar numeros!")
        else:
            print("No puedes escribir caracteres especiales, solo numeros!")
    else:
        print("Solo debe ingresarse un digito!")


def seleccionar_categorias(url):
    categorias = list(os.listdir(url))
    indice_categorias = 1
    opcion = ''
    print("\t--- Selecciona una Categoria---")
    for cat in categorias:
        print(f"\t\tOpcion {indice_categorias} - {cat}")
        indice_categorias += 1
    opcion = input("\nIngresa una opcion: ")
    return int(opcion) - 1


def mostrar_recetas(url, categoria):
    recetas = []
    for cat in Path(url / categoria).glob("*.txt"):
        recetas.append(cat.name)
    return recetas


def elegir_receta(recetas):
    cantidad = len(recetas)
    if cantidad > 0:
        print("--- Escoge una Opcion ---")
        contador = 1
        opcion = ''
        for r in recetas:
            print(f"opcion - {contador}: {r}")
            contador += 1
        opcion = input("¿Cual quieres leer?: ")
        return recetas[int(opcion) - 1]
    else:
        system("cls")
        print("La Categoria esta vacia!")


def leer_receta(url, categoria, receta):
    if receta is not None:
        verificar_receta = Path(url / categoria / receta).exists()
        if verificar_receta:
            archivo = Path(url / categoria / receta).read_text()
            print(archivo)
            opcion = ''
            while opcion != 's':
                opcion = input("¿Esta listo para salir? s/n: ")
            system('cls')
            return True
        else:
            return False


def crear_receta(url, categoria):
    global nombre_receta
    system("cls")
    url_categoria = url / categoria
    opcion = ''
    nueva_receta = ''
    while opcion != 's':
        nombre_receta = input("Ingresa el nombre de la receta: ")
        print("¿Esta seguro que este es el nombre que quiere usar?")
        opcion = input("Ingresa la 's' para confirmar: ")
        system("cls")
        nueva_receta = nombre_receta+".txt"
    respuesta = Path(url_categoria / nueva_receta).exists()
    if not respuesta:
        open(Path(url_categoria / nueva_receta), 'w')
        print(f"se ha creado el archivo {nueva_receta} en el directorio: {url_categoria}")
    else:
        print("La receta ya existe!")


def crear_categoria(url):
    opcion = ''
    nueva_categoria = ''
    while opcion != 's':
        system("cls")
        nueva_categoria = input("Ingrese el nombre de la nueva categoria: ")
        opcion = input("Esta seguro que quiere usar este nombre? 's' para confirmar: ")
    directorio = url / nueva_categoria
    consulta = Path(directorio).exists()
    if not consulta:
        os.makedirs(directorio)
        print(f"se ha creado la categoria: {nueva_categoria} en el directorio: {directorio}")
    else:
        print("La categoria que intenta crear ya estaba registrada!")


def eliminar_receta(url, categoria, receta):
    direccion = Path(url / categoria / receta)
    os.remove(direccion)
    print(f"Se elimino la Receta: {receta}")


def eliminar_categoria(url, categoria):
    direccion = Path(url / categoria)
    os.rmdir(direccion)
    print("Directorio Eliminado!")


def menu_opciones(recetarios):
    opcion = ''
    recetas = []
    while opcion != 6:
        categorias = list(os.listdir(recetarios))
        print("""
            --- Menu de Opciones---
            Opcion 1 - Leer receta
            Opcion 2 - Crear receta
            Opcion 3 - Crear categoria
            Opcion 4 - Eliminar receta
            Opcion 5 - Eliminar categoria
            Opcion 6 - Finalizar sistema
        """)
        opcion = input("¿Que quieres hacer?: ")
        system("cls")
        opcion = validar_datos(opcion)
        if opcion == 1:
            indice_receta = seleccionar_categorias(recetarios)
            recetas = mostrar_recetas(recetarios, categorias[indice_receta])
            receta_elegida = elegir_receta(recetas)
            leer_receta(recetarios, categorias[indice_receta], receta_elegida)
        elif opcion == 2:
            indice_receta = seleccionar_categorias(recetarios)
            crear_receta(recetarios, categorias[indice_receta])
        elif opcion == 3:
            crear_categoria(recetarios)
        elif opcion == 4:
            indice_receta = seleccionar_categorias(recetarios)
            recetas = mostrar_recetas(recetarios, categorias[indice_receta])
            system("cls")
            receta_elegida = elegir_receta(recetas)
            system("cls")
            eliminar_receta(recetarios, categorias[indice_receta], receta_elegida)
        elif opcion == 5:
            indice_receta = seleccionar_categorias(recetarios)
            eliminar_categoria(recetarios, categorias[indice_receta])




system("cls")
print("Hola, Bienvenido a mi recetario!")
recetarios = Path("C:/Users/56992/Documents/python/Dia 6/Recetas")
informar_ruta(recetarios)
numero_recetas = contar_recetarios_totales(recetarios)
print(f"El numero total de recetas es/son: {numero_recetas}")

menu_opciones(recetarios)