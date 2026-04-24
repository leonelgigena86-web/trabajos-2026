class Persona:
    def inicializar(self,nom,edad):
        self.nombre=nom
        self.edad=edad=int(input("ingrese edad: "))
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
persona1=Persona()
persona1.inicializar("Leonel","Edad")
persona1.mostrar()
if persona1.edad>18:
    print("ES MAYOR DE EDAD")
else:
    print("NO ES MAYOR DE EDAD")