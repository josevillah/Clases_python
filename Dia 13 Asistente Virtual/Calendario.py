import datetime

class Calendario:
    momento = None
    hora = datetime.datetime.now()
    fecha = datetime.date.today()
    calendario = {
        0: 'Lunes',
        1: 'Martes',
        2: 'Miércoles',
        3: 'Jueves',
        4: 'Viernes',
        5: 'Sábado',
        6: 'Domingo'
    }
    dia = None

    def ___init__(self):
        self.momento = self.momento
        self.hora = self.hora
        self.fecha = self.fecha
        self.calendario = self.calendario


    def horaDia(self):
        if self.hora.hour < 6 or self.hora.hour > 20:
            self.momento = 'Buenas noches'
        elif self.hora.hour >= 6 and self.hora.hour < 12:
            self.momento = 'Buen día'
        else:
            self.momento = 'Buenas tardes'
        return self.momento

    def queDiaEsHoy(self):
        self.dia = self.fecha.weekday()
        return f'Hoy es {self.calendario[self.dia]}'


    def horaActual(self):
        return f'En este momento son las {self.hora.hour} horas con {self.hora.minute} minutos.'
    