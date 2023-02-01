def devolver_distintos(num1, num2, num3):
    mayor = max(num1,num2,num3)
    menor = min(num1,num2,num3)
    suma = num1 + num2 + num3
    if suma >= 15:
        return mayor
    elif suma < 10:
        return menor
    elif 10 >= suma <= 15:
        return 15 - 10


resultado = devolver_distintos(4, 4, 7)
print(resultado)