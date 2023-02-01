from random import shuffle
# Lista inicial
palitos = ['-','--','---','----']
# mesclar palitos
def mesclar(lista):
    shuffle(lista)
    return lista
# Pedirle intento
def suerte():
    intento = ''
    while intento not in ['1','2','3','4']:
        intento = input("Elige un numero del 1 al 4: ")
    return int(intento)
# Comprobar intento
def comprobar(lista,intento):
    if lista[intento - 1] == '-':
        print(f"A limpiar te toco el palito mas corto")
    else:
        print("JAJAJa te salvaste")

    print(f"te toco {lista[intento - 1]}")

mescla = mesclar(palitos)
seleccion = suerte()
comprobar(mescla,seleccion)