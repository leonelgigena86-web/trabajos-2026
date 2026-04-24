import random

class Objeto():
    def __init__(self,nombre):
        self.nombre=nombre

class Aventurero():
    def __init__(self,nombre):
        self.nombre=nombre=input("Ingrese su nombre, aventurero/a: ")
        self.inventario=[]
    def guardar(self,objeto):
        self.inventario.append(objeto)
        print(self.nombre,"guardó",objeto.nombre)
    def usar(self,objeto):
        print(self.nombre,"usó",objeto.nombre)
    def descartar(self,objeto):
        print(self.nombre,"descartó",objeto.nombre)
    def mostrar_inventario(self):
        print("\nInventario:")
        if len(self.inventario) == 0:
            print("No hay nada, guardá algún objeto")
        else:
            for obj in self.inventario:
                print("-",obj.nombre)

jugador=Aventurero("Leo")
objetos_posibles=["Espada","Poción de curación","Escudo","Llave","Mapa","Poción de la juventud eterna","Lápiz","Goma","Pelota de fútbol","Pico"]

while True:
    print()
    objeto=Objeto(random.choice(objetos_posibles))
    print("\nEncontraste:", objeto.nombre)
    print("1-Guardar")
    print("2-Usar")
    print("3-Descartar")
    print("4-Ver inventario")
    print("5-Salir")
    decision = input("Elige opción, por favor: ")
    print()
    if decision == "1":
        jugador.guardar(objeto)
    elif decision == "2":
        jugador.usar(objeto)
    elif decision == "3":
        jugador.descartar(objeto)
    elif decision == "4":
        jugador.mostrar_inventario()
    elif decision == "5":
        print("Recorrido finalizado")
        break