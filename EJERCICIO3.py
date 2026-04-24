class Triangulo:
    def inicializar(self, lado):
        self.lado1 = lado1 = int(input("Ingrese el valor del lado 1: "))
        self.lado2 = lado2 = int(input("Ingrese el valor del lado 2: "))
        self.lado3 = lado3 = int(input("Ingrese el valor del lado 3: "))
    
    def mostrar(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero.")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("El triángulo es isósceles.")
        else:
            print("El triángulo es escaleno.")     
triangulo1=Triangulo()
triangulo1.inicializar("Lados")
triangulo1.mostrar()    
        
    