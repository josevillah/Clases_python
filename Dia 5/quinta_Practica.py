# Juego del ahorcado
# hacer una lista con palabras
# mostrar una serie de guiones que representa la palabra
# En cada turno el jugador debe ingresar una legra
# si el jugador acierta con la letra debe mostrar en donde se encuenta y reemplazar el guien anterior
# si el jugador ingresa una letra que no se encuenta dentro de la palabra, este pierde una vida
# si el jugador agota las vidas, este perdera 6 vidas
# si el jugador acierta la palabra, Gana

from random import choice

lista_palabras = [
    'Saludo',
    'Comida',
    'Bebida',
    'Animal',
    'Pez',
    'Programacion',
    'Saturno',
    'Hijos',
    'Padres',
    'Grito',
    'Perdon',
    'Luna',
    'Problema',
    'Feliz',
    'Avenida',
    'Fuerte',
    'Teclado',
    'Tener',
    'Amor',
    'Olas',
    'Vos',
    'Hacer'
]

palabra = list(choice(lista_palabras))
tamanio = len(palabra)

vida = 6
adivina = list('-'*tamanio)
adivina2 = list('-'*tamanio)

# print(f"Esta es la Palabra: {'-'*tamanio}")
# print(palabra)
print(f"Esta es la Palabra: {adivina}")

while vida > 0:

    if adivina != adivina2:
        # adivina2 = []
        adivina2 = list(adivina)
    else:
        vida -= 1

    print(f"Tienes {vida} vida/s")
    letra = input("Ingresa una letra que creas que forma parte de la palabra: ")
    indice = 0
    for l in palabra:
        if letra == l.lower():
            adivina[indice] = l
            indice += 1
        else:
            indice += 1
    if adivina != palabra:
        print(adivina)
    else:
        print(f"Has Ganado!!")
        break


else:
    print("Game Over")