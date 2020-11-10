palos = ["o", "c", "e", "b"]
numeros = ["A", "2", "3", "4", '5', '6', '7', 'S', 'C', 'R']

#creacion de la baraja
def crearBaraja():
    baraja = []
    for palo in palos:
        for numero in numeros:
            baraja.append(numero+palo)
    return baraja


