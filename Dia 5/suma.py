'''
Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y
retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume,
o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).
'''

def suma_absolutos(*args):
    total = 0
    for arg in args:
        if arg < 0:
            total += arg*(-1)
        else:
            total += arg
    return total
total = suma_absolutos(-5,-4,-3,-2,-1,0,1,2,3,4,5)
print(total)

