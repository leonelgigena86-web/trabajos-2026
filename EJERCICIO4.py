class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1=int(input("Ingrese el primer número: "))
        self.num2 = num2=int(input("Ingrese el segundo número: "))
        
    def sumar(self):
        return self.num1 + self.num2
    
    def restar(self):
        return self.num1 - self.num2
    
    def multiplicar(self):
        return self.num1 * self.num2
    
    def dividir(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: División por cero"
calculadora1 = Calculadora("Numero1", "Numero2") 
print("Suma: ", calculadora1.sumar())
print("Resta: ", calculadora1.restar()) 
print("Multiplicación: ", calculadora1.multiplicar())
print("División: ", calculadora1.dividir())