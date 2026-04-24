class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print(self.titular, "tiene $", self.cantidad, "dólares")

class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes
        self.interes_total = 0
    def importe_interes(self):
        self.interes_total = self.cantidad * self.interes / 100
    def mostrar(self):
        print("La cuenta le pertenece a", self.titular)
        print("Plazo:", self.plazo, "meses")
        print("Interés:", self.interes, "%")
        print("Interés total:", self.interes_total)

class CajaAhorro(Cuenta):
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)

persona1 = Cuenta("Juan", 1000)
persona1.mostrar()
persona1 = PlazoFijo("Juan", 1000, 12, 5)
persona1.importe_interes()
persona1.mostrar()
persona1 = CajaAhorro("Juan", 1000)
persona1.mostrar()