
import baraja
class Baraja():

    def __init__(self, palos, numeros):
        self.palos = palos
        self.numeros = numeros
        self.mazacote = baraja.crearBaraja(palos, numeros)
    def barajar(self):
        baraja.barajar(self.mazacote)


    def repartir(self, num_jugadores, num_cartas):
        jugadores = []
        #crear listas dentro de listas
        for i in range(num_jugadores):
            jugadores.append([])

        for carta in range(num_cartas):
            for jugador in range(num_jugadores):
                #añadame lo que me has quitado
                jugadores[jugador].append(self.mazacote.pop(0))
        return jugadores
