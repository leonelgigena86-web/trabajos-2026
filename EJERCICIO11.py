import random

class Hechicero():
    def __init__(self,nombre):
        self.nombre=nombre=input("Ingrese su nombre: ")
        self.vida=vida=100
        self.energía=energía=50
    def atacar(self,enemigo):
        daño=random.randint(5,15)
        enemigo.vida-=daño
        print(self.nombre,"hizo",daño,"de daño")
    def hechizo(self,enemigo):
        if self.energía>=15:
            daño=random.randint(10,20)
            enemigo.vida-=daño
            print(self.nombre,"uso hechizo, e infligió",daño,"de daño")
        else:
            print("Ay",self.nombre,"te falta energía, curate o usa las manos")
    def curar(self):
        if self.energía>=10:
            cura=random.randint(15,25)
            self.vida+=cura
            self.energía-=10
        else:
            print("Que pena",self.nombre,"me parece que te quedas sin muchas opciones, usa las manos")
    def mostrar_estado(self):
        print("El hechicero",self.nombre,"tiene",self.vida,"de vida. Continua con la batalla")

Jugador=Hechicero("Bueno")
enemigo=Hechicero("Malo")

while Jugador.vida>0 and enemigo.vida>0:
    print("Elige una de las siguiente opciones YA")
    print()
    print("1-Ataca")
    print("2-Hechizo")
    print("3-Curar")
    print()
    decisión=input("DALE DALE, ELEGÍ: ")
    if decisión=="1":
        Jugador.atacar(enemigo)
    elif decisión=="2":
        Jugador.hechizo(enemigo)
    elif decisión=="3":
        Jugador.curar()
    acción=random.choice([1,2,3])
    if acción==1:
        enemigo.atacar(Jugador)
    elif acción==2:
        enemigo.hechizo(Jugador)
    elif acción==3:
        enemigo.curar()
    Jugador.mostrar_estado()
    enemigo.mostrar_estado()
if Jugador.vida>0:
    print("¿Ves que si podías ganar? Te tuve fé")
else:
    print("A llorar en el campito")