class Agenda:
    def inicializar(self, nombre, telefono, email):
        self.nombre = nombre=input("Ingrese el nombre: ")
        self.telefono = telefono=int(input("Ingrese el teléfono: "))
        self.email = email=input("Ingrese el email: ")
        
    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Teléfono: ", self.telefono)
        print("Email: ", self.email)
agenda1=Agenda()
print("1.añadir contacto")
print("2.mostrar contacto")
print("3.buscar contacto")
print("4.editar contacto")
print("5.eliminar agenda")
op=int(input("ingrese opcion: "))
while op!=5:
    if op==1:
        agenda1.inicializar("Nombre", "Telefono", "Email")
    elif op==2:
        agenda1.mostrar()
    elif op==3:
        nombre_buscar=input("Ingrese el nombre a buscar: ")
        if agenda1.nombre == nombre_buscar:
            print("Contacto encontrado:")
            agenda1.mostrar()
        else:
            print("Contacto no encontrado.")
    elif op==4:
        nombre_editar=input("Ingrese el nombre del contacto a editar: ")
        if agenda1.nombre == nombre_editar:
            print("Contacto encontrado. Ingrese los nuevos datos:")
            agenda1.inicializar("Nombre", "Telefono", "Email")
        else:
            print("Contacto no encontrado.")
    else:
        print("Opción no válida.")
    op=int(input("ingrese opcion: "))
    
