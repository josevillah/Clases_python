"""
Crea una clase llamada Casa, y asígnale atributos: color, cantidad_pisos.

Crea una instancia de Casa, llamada casa_blanca, de color "blanco" y cantidad de pisos igual a 4.
"""


class Casa:

    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos


class Cubo:
    cara = 6

    def __init__(self, color):
        self.caras = color

cubo_rojo = Cubo('rojo')
print(cubo_rojo.color)
print(cubo_rojo.ejemplo)
"""casa_blanca = Casa()
casa_blanca.color = "blanco"
casa_blanca.cantidad_pisos = 4"""
