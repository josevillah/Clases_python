def reducir_lista(lista1):
    lista_numeros = []
    for e in lista1:
        if e not in lista_numeros:
            lista_numeros.append(e)
    maximo = max(lista_numeros)
    lista_numeros.remove(maximo)
    return lista_numeros


def promedio(lista2):
    suma = 0
    for nota in lista2:
        suma = suma + int(nota)
    return suma / len(lista2)

lista = [1, 1, 2, 3, 3, 4, 4, 5, 6]

nueva_lista = reducir_lista(lista)
promedio(nueva_lista)