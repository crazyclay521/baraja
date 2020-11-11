import random
palos = ["o", "c", "e", "b"]
numeros = ["A", "2", "3", "4", '5', '6', '7', 'S', 'C', 'R']

#creacion de la baraja
def crearBaraja():
    baraja = []
    for palo in palos:
        for numero in numeros:
            baraja.append(numero+palo)
    return baraja
print(crearBaraja())

def barajarBaraja():
    baraja = crearBaraja()
    for i in range(40):
        intercanbioCartas()
        y = random.randint(0, 39)
        baraja[i] = baraja[y]
    return baraja
def intercambioCartas():
    baraja = crearBaraja()
    cartaVacia = ()
    cartaVacia = baraja[i]
    baraja[i] = baraja[y]
    baraja[y] = cartaVacia
    return baraja[i], baraja[y]



y = barajarBaraja()
print(y)
