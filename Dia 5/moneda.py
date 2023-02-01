''''
Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.

Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).

Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).

Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.

Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.
'''

from random import choice
def lanzar_moneda():
    moneda = ['Cara', 'Cruz']
    return choice(moneda)

def probar_suerte(moneda, lista_numeros):
    if "Cara" in moneda:
        print(f"La lista se autodestruirá")
        lista_numeros = []
        return lista_numeros
    elif "Cruz" in moneda:
        print(f"La lista fue salvada")
        return lista_numeros

moneda = lanzar_moneda()
lista_numeros = list(range(-100,26))
result = probar_suerte(moneda, lista_numeros)
print(result)