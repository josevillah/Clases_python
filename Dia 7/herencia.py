class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print(f"He nacido desde mi clase padre")


class Pajaro(Animal):
    pass


julio = Pajaro(2,"azul")
julio.nacer()