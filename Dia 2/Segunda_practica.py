# Los vendedores tienen Comisiones del 13%
# Preguntar Nombre y monto vendido

# y el sistema debe decir: ok juan. Este mes ganaste $650 de comision

comision = 13 / 100
nombre = input("¿Cual es tu nombre? ")
total_ventas = input("¿Cuanto vendiste en el mes? ")

print(f"Ok {nombre}. Este mes ganaste ${round(float(total_ventas)*comision)} de comision")