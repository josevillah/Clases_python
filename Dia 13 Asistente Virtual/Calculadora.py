class Calculadora:
    resultado = 0

    def __init__(self):
        self.resultado = self.resultado
        
    
    def verify(self, texto):
        self.resultado = 0
        for signo in texto:
            if not signo.isdecimal():
                if signo == '+':
                    return self.suma(texto)

    def suma(self, texto):
        for i in texto:
            if i.isdecimal():
                self.resultado+= int(i)
        return self.resultado

    def resta(self, texto):
        sum=0
        for i in texto:
            if i.isdecimal():
                sum -= int(i)
        return sum

    def multiplicar(self, texto):
        pass

    def dividir(self, texto):
        pass