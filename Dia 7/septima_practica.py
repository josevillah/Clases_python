"""
 1- crear una clase llamada persona con los atributos nombre y apellido
 2- crear una clase cliente que hereda de persona con atributis propios: número de cuenta y balance
    2.1- crear metodo imprimir cliente
    2.2- crear metodo para depositar
    2.3- crear metodo para retirar
 3- menu que contenga: depositar, retirar y salir
"""
from os import system


class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __int__(self):
        return f"{self.balance}"

    def mostrar_cliente(self):
        print(f"Bienvenido {self.nombre} {self.apellido}")
        print(f"Tu numero de cuenta es: {self.numero_cuenta}")
        print(f"Balance: ${self.balance}")

    def depositar(self):
        monto = input("Ingresa monto a depositar: ")
        self.balance += int(monto)
        print(f"Monto depositado")

    def retirar(self):
        monto = input("Ingresa cuanto quieres retirar: ")
        self.balance -= int(monto)


def registro():
    system("cls")
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    numero = int(input("ingresa el numero de cuenta: "))
    balance = int(input("Ingresa tu balance: "))
    iniciar(nombre, apellido, numero, balance)


def iniciar(nombre, apellido, numero, balance):
    perso = Cliente(nombre, apellido, numero, balance)
    opcion = ''
    while opcion != 3:
        system("cls")
        perso.mostrar_cliente()
        print("\n")
        print("*****Menu de Opciones*****")
        print("[1]: Depositar")
        print("[2]: Retirar")
        print("[3]: Salir")
        opcion = int(input("opcion: "))
        if opcion == 1:
            system("cls")
            perso.depositar()
        elif opcion == 2:
            system("cls")
            perso.retirar()
        elif opcion == 3:
            system("cls")
            print("Vuelve Pronto!")


registro()
