class Pajaro:

    def __int__(self, color, especie):
        self.color = color
        self.especie = especie


mi_pajaro = Pajaro()
mi_pajaro.color = "Rojo"
mi_pajaro.especie = "Carpintero"

print(f"El pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")
