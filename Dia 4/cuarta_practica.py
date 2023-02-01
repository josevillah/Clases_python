#Preguntar al usuario su nombre
#luego debe imprimir nombre pense en un numero del 1 al 100 y tienes 8 intentos para adivinarlo, ¿Cual crees que es el numero?
#ingresar un numero
#menor a 1 o mayor a 100 informar que el numero ingresado no esta permitido
#si el numero es menor al que el programa penso le dira que es incorrecto y que el numero ingresado es menor al pensado
#si el numero es mayor hara lo mismo que el paso anterior
#si se acierta, se le indica que ha ganado y cuandos intentos le tomo para adivinarlo
#si el usuario no adivina en los 8 intentos se le dice has perdido
from random import randint
nombre = input("Cual es tu nombre? ")
print(f"Hola {nombre} Que te parese si jugamos algo?")
print(f"{nombre} Pensare en un numero del 1 al 10 y tu tienes que adivinarlo, pero ojo, solo tienes 3 INTENTOS")
intentos = 3
intentos_totales = 8
valor_pensado = randint(1, 10)
while intentos > 0:
    numero = int(input(f"Ingresa el numero: "))
    if numero == valor_pensado:
        print(f"Siiii! Lo conseguiste mi numero era: {numero} y lo conseguiste en {intentos_totales - intentos} intentos")
        break
    elif numero <= 0:
        print(f"Es un numero del uno al 100, o no entendiste? -.-")
    elif numero > 100:
        print(f"Es un numero del uno al 100, no te pases")
    else:
        intentos = intentos - 1
        print(f"Ese no es el que habia pensado jajaja, te quedan {intentos}")
else:
    print(f"Me encanta cuando pasa esto!")
    print(f"El numero era {valor_pensado}")
    print(f"{nombre} GAME OVER!!!")