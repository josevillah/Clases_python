class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")


gandalf = Mago()
legolas = Arquero()
riquimaru = Samurai()

personajes = [legolas, gandalf, riquimaru]

for persona in personajes:
    persona.atacar()