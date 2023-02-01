"""
    Sistema Turnero.
    Tiene 3 áreas
    perfumeria, farmacia y cosmeticos
    letras: P, F, C

    los mensajes en los papeles son:
        Su turno es:
            P-01,
    espere y sea atendido

    2 archivos:
     1- modulos.py
        generadores y decoradores
     2- principal.py
        funciones del sistema
"""

from modulos import *
from os import system


def categoria(opcion):
    sector = ''
    letra = ''
    if opcion == 1:
        sector = turno_perfumeria()
        letra = 'P'
    elif opcion == 2:
        sector = turno_farmacia()
        letra = 'F'
    elif opcion == 3:
        sector = turno_cosmeticos()
        letra = 'C'

    return letra, sector


def iniciar():
    intento = True
    while intento:
        try:
            opcion = int(input("Ingresa una opcion: "))
        except:
            print("Has ingresado un dato erroneo")
        else:
            print("si")
            letra, sector = categoria(opcion)
            print("Su turno es:")
            print(f"{letra}-{next(sector)}")
            print(f"{letra}-{next(sector)}")
            print("espere y sera atendido")


iniciar()
