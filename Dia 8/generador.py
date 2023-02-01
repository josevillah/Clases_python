# Esta funcion retorna una lista con los numeros del 1 al 10
def mi_funcion():
    lista = []
    for n in range(1, 11):
        lista.append(n)
    return lista


# Esta funcion genera un número de una lista interna que se va desarrollando cada vez que es pedida
def generador():
    for n in range(1, 11):
        yield n


mi_funcion()
mi_generador = generador()
print(next(mi_generador))
print(next(mi_generador))
print(next(mi_generador))