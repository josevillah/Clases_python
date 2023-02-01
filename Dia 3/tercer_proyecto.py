#permitir al usuario ingresar un texto
#permitir al usuario ingresar 3 letras cualquiera
#debe devolver cuantas veces aparecen cada una de las letras que ingreso antes
#hay que decirle al usuario cuantas palabras hay en el texto
#indicar cual es la primera y ultima letra
# mostrar el texto invertido
#que el sistema diga si la palabra python esta en el texto escrito

texto = input("ingrese el texto deseado: ")
print("Tendras que ingresar 3 letras aleatorias, las que mas gustes!")
letra1 = input("Primera letra: ")
letra2 = input("Segunda letra: ")
letra3 = input("Tercera letra: ")
texto = texto.lower()
print("Letras ingresadas con exito!")
print(f"La cantidad de la primera letra es: {texto.count(letra1)}")
print(f"La cantidad de la Segunda letra es: {texto.count(letra2)}")
print(f"La cantidad de la Tercera letra es: {texto.count(letra3)}")
print("calculando cuantas palabras tiene el texto que ingresó...")
texto2 = texto.split()
print(f"La cantidad de palabras ingresadas es/son: {len(texto2)}")
print(f"La primera letra del texto es: {texto[0]}")
print(f"La ultima letra del texto es: {texto[len(texto)-1]}")
print(f"El texto al revés, es: \n {texto[::-1]}")
print(f"¿La palabra python esta escrita en el texto?: {'python' in texto}")
