class Pajaro:

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f"Soy Piolin y soy un {self.especie} de color {self.color}, Me parecio ver un lindo gatito")


piolin = Pajaro("Amarillo", "Canario")

piolin.piar()