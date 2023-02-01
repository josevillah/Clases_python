def letras_unicas(palabra):
    nueva_palabra = []
    for letra in palabra:
        if letra not in nueva_palabra:
            nueva_palabra.append(letra)
    nueva_palabra.sort()
    return nueva_palabra


resultado = letras_unicas("programacion")
print(resultado)