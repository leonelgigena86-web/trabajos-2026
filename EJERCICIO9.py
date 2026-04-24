import random

class Tesoro_normal():
    def abrir(self):
        self.abierto=abierto=random.choice([True,False])     
    def mostrar_tesoro(self):
        if self.abierto:
            self.monedas=random.randint(5,15)
            print("El tesoro está abierto y tiene ", self.monedas, "monedas")
        else:
            print("El tesoro está cerrado y no puedes agarrar las monedas")
            
class Tesoro_trampa():
    def abrir(self):
        self.abierto=abierto=random.choice([True,False])    
    def mostrar_tesoro(self):
        if self.abierto:
            print("Caiste en una trampa, pierdes 20 de energía. JODETE")
        else:
            print("El tesoro está cerrado y no puedes agarrar las monedas")
            
class Explorador():
    def __init__(self,nombre,energia):
        self.nombre=nombre
        self.energia=energia=100
        self.total_monedas=0
        print(self.nombre, "tiene ", self.energia, "de energía")
    def recolectar_monedas(self,tesoro):
        if tesoro.abierto==False:
         return 
    
        if isinstance(tesoro, Tesoro_normal) :
            print("¿Quieres recolectar las monedas del tesoro?")
            decision = input()
            if decision == "si":
                print(self.nombre, "recolectó ", tesoro.monedas, "monedas")
                self.total_monedas += tesoro.monedas
                self.energia += tesoro.monedas
            else:
                print(self.nombre, "se jodió por las monedas especiales")
        elif isinstance(tesoro, Tesoro_trampa):
            self.energia -= 20
            print(self.nombre, "perdió 20 de energía por la trampa y ahora tiene ", self.energia, "de energía")

jugador=Explorador("Leo", 100)
tesoro=random.choice([Tesoro_normal(), Tesoro_trampa()])
while jugador.energia > 0:
    print("Encontraste un tesoro,decides abrirlo?")
    print()
    decision = input()
    if decision == "abrir":
        tesoro.abrir()
        print()
        tesoro.mostrar_tesoro()
        print()
        jugador.recolectar_monedas(tesoro)
        print()
    else:
        print("Te jodiste, era tu oportunidad")
        print()
    print(jugador.nombre, "tiene ", jugador.energia, "de energía y ", jugador.total_monedas, "monedas")
    print()
    tesoro=random.choice([Tesoro_normal(), Tesoro_trampa()])
print("Hiciste despertar al oso que dormía la siesta")
print()
print("GAME OVER")
