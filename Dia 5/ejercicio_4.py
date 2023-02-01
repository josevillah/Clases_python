def contar_primos(num):
    primos = [2]
    iteracion = 3

    if iteracion < 2:
        print(f"el numero que ingresaste no es primo, ingresa un numero mas alto que: {num}")
        return 0

    while iteracion <= num:
        for n in range(3,iteracion,2):
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2

    print(primos)
    return len(primos)



print(contar_primos(1000))