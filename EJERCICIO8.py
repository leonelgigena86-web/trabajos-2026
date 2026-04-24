import random
class Personaje():
    def __init__(self, daño, vida, nombre):
        self.nombre = nombre=input("Ingrese el nombre del personaje: ")
        self.daño = daño=random.randint(5, 15)
        self.vida = vida=random.randint(50, 100)
    def atacar(self, enemigo):
        enemigo.vida -= self.daño
    def mostrar_estado(self):
        print(f"{self.nombre} tiene {self.vida}HP.")
class  Jugador(Personaje):
    def __init__(self, daño, vida, nombre):
        super().__init__(daño, vida, nombre)
class Enemigo(Personaje):
    def __init__(self, daño, vida, nombre):
        super().__init__(daño, vida, nombre)
jugador1 = Jugador(10, 100, "Bueno")
enemigo1 = Enemigo(5, 50, "Malo")
while jugador1.vida > 0 and enemigo1.vida > 0:
    op=ingres=int(input("Ingrese 1 para atacar o 2 para mostrar estado de vida: "))
    if op==1:
        jugador1.atacar(enemigo1)
        print("Has hecho, ", jugador1.daño, "de daño")  
    elif op==2:
        jugador1.mostrar_estado()
    enemigo1.atacar(jugador1)
    print("El enemigo te hizo, ", enemigo1.daño, "de daño")
    enemigo1.mostrar_estado()
    if jugador1.vida <= 0 or enemigo1.vida <= 0:
        break
if jugador1.vida <= 0:
    print(f"Te ha ganado el sistema")
if enemigo1.vida <= 0:
    print(f"Has ganado al sistema")
