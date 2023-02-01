class CD:

    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f'Albun {self.titulo} de {self.autor}'

    def __len__(self):
        return self.canciones

    def __del__(self):
        print("Se ha eliminado mi CD")


mi_cd = CD("Pink Floyd", "The Wall", 24)

del mi_cd