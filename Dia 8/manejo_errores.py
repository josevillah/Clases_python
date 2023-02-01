def suma():
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    print("Gracias por sumar")


try:
    # Codigo que se quiere probar
    suma()
except:
    # Codigo a ejecutar si hay algún error
    print("Algo paso!")
else:
    # Este es el codigo que se va a ejecutar si no hay error
    print("Hiciste todo Bien!")
finally:
    # Codigo que se ejecuta de todos modos
    print("Eso fue todo")
