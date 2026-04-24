import random

class Auto():
    def __init__(self,nombre):
        self.nombre=nombre=input("Ingrese su nombre: ")
        self.velocidad=0
        self.metro=0
    def acelerar(self):
        self.velocidad=velocidad=60
    def frenar(self):
        if self.velocidad>0:
            self.velocidad-=20
    def posicion(self):
        self.metro+=self.velocidad
    def mostrar_estado(self):
        print("El competidor", self.nombre,"va con", self.metro,"metros recorridos, a una velocidad de", self.velocidad)

Jugador=Auto("Leo")
corredor2=Auto("Pepe")
corredor3=Auto("Carlos")
meta=1000

while Jugador.metro<meta and corredor2.metro<meta and corredor3.metro<meta:
    print("¿Que acción desea realizar?")
    print()
    print("1-Acelerar")
    print("2-Frenar")
    print("3-Mantener velocidad")
    print()
    decision=input("Ingrese acción realizada: ")
    if decision=="1":
        Jugador.acelerar()
    elif decision=="2":
        Jugador.frenar()
    Jugador.posicion()
    acción=random.choice(["Acelerar","Mantener","Frenar"]) 
    if acción=="Acelerar":
        corredor2.acelerar()
    elif acción=="Frenar":
        corredor2.frenar()
    corredor2.posicion()
    acción2=random.choice(["Acelerar","Mantener","Frenar"])
    if acción2=="Acelerar":
        corredor3.acelerar()
    elif acción2=="Frenar":
        corredor3.frenar()
    corredor3.posicion()
    Jugador.mostrar_estado()
    corredor2.mostrar_estado()
    corredor3.mostrar_estado()
    print()
if Jugador.metro>meta:
    print("Felicidades, has ganado la carrera. Nos veremos en el World Grand Prix")
else:
    print("Has perdido la carrera con ",Jugador.metro,"metros recorridos")