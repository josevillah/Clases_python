import time
import timeit


def funcion1(num):
    lista = []
    for n in range(1, num):
        lista.append(n)
    return lista


def funcion2(num):
    lista = []
    contador = 1
    while contador != num:
        lista.append(contador)
        contador += 1
    return lista


inicial = time.time()
print(funcion1(10001))
final = time.time()
print(final-inicial)


inicial = time.time()
print(funcion2(10001))
final = time.time()
print(final-inicial)


"""timeit"""


print("\n")
print("\n")

declaracion = """
funcion1(10)
"""

mi_setup = """
def funcion1(num):
    lista = []
    for n in range(1, num):
        lista.append(n)
    return lista
"""

duracion = timeit.timeit(declaracion, mi_setup, number=1000000)
print(duracion)

declaracion = """
funcion2(10)
"""

mi_setup = """
def funcion2(num):
    lista = []
    contador = 1
    while contador != num:
        lista.append(contador)
        contador += 1
    return lista
"""
duracion2 = timeit.timeit(declaracion, mi_setup, number=1000000)
print(duracion2)
