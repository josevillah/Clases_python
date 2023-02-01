def cero_repetidos(*args):
    lista = []
    for arg in args:
        lista.append(arg)
    lista2 = []
    result = bool
    for n in lista:
        posicion = len(lista2)
        lista2.append(n)
        if posicion >= 0:
            if 0 == n:
                if n == lista2[posicion - 1]:
                    result = True
                elif n != lista2[posicion - 1]:
                    result = False
    return result


numarg = 6, 0, 5, 1, 0, 3, 0, 1
# numarg = 5, 6, 1, 0, 0, 9, 3, 5
resultado = cero_repetidos(*numarg)
if not resultado:
    print(f"en la lista {numarg} se encontro el resultado: {resultado}")
else:
    print(f"en la lista {numarg} se encontro el resultado: {resultado}")