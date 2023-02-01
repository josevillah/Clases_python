def turno_perfumeria():
    for n in range(1, 301):
        yield n


def turno_farmacia():
    turno = True
    opcion = 0
    while turno:
        opcion += 1
        yield opcion


def turno_cosmeticos():
    turno = True
    opcion = 0
    while turno:
        opcion += 1
        yield opcion
