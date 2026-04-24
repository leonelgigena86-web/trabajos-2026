class Alumno:
    def inicializar(self,nom,nota):
        self.nombre=nom
        self.notita=nota=int(input("ingrese nota: "))
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Nota: ",self.notita)
alumno1=Alumno()
alumno1.inicializar("Leonel","Nota")
alumno1.mostrar()
if alumno1.notita>7:
    print("APROBADO")
else:
    print("DESAPROBADO")