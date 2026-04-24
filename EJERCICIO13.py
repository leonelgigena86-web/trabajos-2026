import random

class Jugador():
    def __init__(self,nombre):
        self.nombre=nombre=input("Ingresa nombre para jugar: ")
        self.puntaje=0
    def lanzar_dado(self):
        valor=random.randint(1,6)
        self.puntaje+=valor
        print(self.nombre,"sacó",valor)

jugador=Jugador("Tú")
enemigo=Jugador("Ana")
enemigo2=Jugador("Luis")
enemigo3=Jugador("Luz")
rondas = 0

while rondas<5:
    print()
    print("\nRonda", rondas+1)
    input("ENTER para lanzar el dado (no le vayas a errar)")
    jugador.lanzar_dado()
    enemigo.lanzar_dado()
    enemigo2.lanzar_dado()
    enemigo3.lanzar_dado()
    print()
    print("Puntajes de los jugadores:")
    print(jugador.nombre, jugador.puntaje)
    print(enemigo.nombre, enemigo.puntaje)
    print(enemigo2.nombre, enemigo2.puntaje)
    print(enemigo3.nombre, enemigo3.puntaje)
    rondas += 1
if jugador.puntaje>enemigo.puntaje and jugador.puntaje>enemigo.puntaje and jugador.puntaje>enemigo3.puntaje:
    print("Ha ganado",jugador.nombre,"con un puntaje de",jugador.puntaje,"puntos")
elif enemigo.puntaje>jugador.puntaje and enemigo.puntaje>enemigo2.puntaje and enemigo.puntaje>enemigo3.puntaje:
    print("Ha ganado",enemigo.nombre,"con un puntaje de",enemigo.puntaje,"puntos")
elif enemigo2.puntaje>enemigo.puntaje and enemigo2.puntaje>jugador.puntaje and enemigo2.puntaje>enemigo3.puntaje:
    print("Ha ganado",enemigo2.nombre,"con un puntaje de",enemigo2.puntaje,"puntos")
elif enemigo3.puntaje>enemigo.puntaje and enemigo3.puntaje>enemigo2.puntaje and enemigo.puntaje>jugador.puntaje:
    print("Ha ganado",enemigo3.nombre,"con un puntaje de",enemigo3.puntaje,"puntos")