class Cliente():
    def __init__(self,nombre,cantidad):
        self.nombre=nombre
        self.cantidad=cantidad=int(input("Ingrese la cantidad disponible de dinero: "))
    def depositar(self, cantidad):
        self.cantidad += cantidad==int(input("Ingrese la cantidad a depositar: "))
    def extraer(self, cantidad):
        monto=int(input("Ingrese la cantidad a extraer: "))
        if self.cantidad >= monto:
            self.cantidad -= monto
        else:
            print("No hay suficiente dinero para extraer.")
    def mostrar_total(self):
        print("Total disponible: ", self.cantidad)
class Banco():
    def __init__(self, nombre):
        self.nombre=nombre
        self.clientes=[]
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
    def mostrar_clientes(self):
        print("Clientes del banco ", self.nombre)
        for cliente in self.clientes:
            print("Nombre: ", cliente.nombre, "Cantidad: ", cliente.cantidad)
    def operar_cliente(self, cliente):
        print("Operaciones para el cliente ", cliente.nombre)
        print("1. Depositar")
        print("2. Extraer")
        print("3. Mostrar total")
        opcion=int(input("Ingrese la opción deseada: "))
        if opcion==1:
            cliente.depositar(0)
        elif opcion==2:
            cliente.extraer(0)
        elif opcion==3:
            cliente.mostrar_total()
        else:
            print("Opción no válida.")
    def deposito_total(self):
        total=0
        for cliente in self.clientes:
            total += cliente.cantidad
        print("Depósito total en el banco: ", total)
cliente1=Cliente("Juan", 1000)
cliente1.depositar(0)
cliente1.extraer(0)
cliente1.mostrar_total()
banco1=Banco("Banco Central")
banco1.agregar_cliente(cliente1)
banco1.mostrar_clientes()
banco1.operar_cliente(cliente1)
banco1.deposito_total()
print("Al final del día, se depositaron $", banco1.deposito_total())