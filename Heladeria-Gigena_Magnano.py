import tkinter as tk

ventana = tk.Tk() #variable para la ventana
ventana.title("Heladería") #titulo de la ventana
ventana.attributes("-fullscreen", True) #pantalla completa
precios = {1:700, 2:1200, 3:1600,}#diccionario con las bochas y su respectivo precio
sabores = ["Chocolate","Vainilla","Frutilla","Dulce de leche","Limón","Sambayón","Marroc",] #lista con todos los sabores disponibles
sabores_elegidos = []#lista vacía para los sabores elegidos
botones_sabores = {}
# ---------- FUNCIONES ----------
def mostrar(frame): #funcion para mostrar las secciones
    frame.tkraise()

def elegir_sabor(sabor): #funcion para elegir el sabor
    if len(sabores_elegidos) < 3: #si llega hasta 3 bochas, se pondra verde
        sabores_elegidos.append(sabor)
        botones_sabores[sabor].config(bg="lightgreen")
        actualizar()
    else: #si sobrepasa el limite de bochas, se pondra rojo
        botones_sabores[sabor].config(bg="red")

def actualizar(): #funcion para actualizar la ventana y secciones
    texto = ""
    for s in sabores_elegidos:
        texto += s + "\n"
    pedido_label.config(text=texto)
    cantidad = len(sabores_elegidos)
    if cantidad in precios:
        precio_label.config(text=f"${precios[cantidad]}")
    else:
        precio_label.config(text="$0")

def reiniciar(): #funcion para reiniciar el pedido una vez confirmado
    sabores_elegidos.clear()
    for boton in botones_sabores.values():
        boton.config(bg="SystemButtonFace")
    actualizar()

def confirmar(): #funcion para confirmar el pedido con sus respectivos sabores
    if len(sabores_elegidos) == 0: #si no se elige un sabor y se confirma, saldra un mensaje en rojo diciendo que elija un sabor
        boton_confirmar.config(
            text="Elige al menos un sabor",
            bg="red",
            fg="white"
        )
    else: #si hay 1 o mas sabores seleccionados, se confirmara el pedido en verde sin reclamo 
        precio_label.config(text="Pedido confirmado ")
        boton_confirmar.config(
            text="Confirmado",
            bg="lightgreen",
            fg="black"
        )

def salir(event): #funcion para salir de la ventana
    ventana.attributes("-fullscreen", False)

ventana.bind("<Escape>", salir) #tecla `para salir de la ventana
# ---------- MENÚ SUPERIOR ----------
menu = tk.Frame(ventana)#menu que muestra la ventana
menu.pack(fill="x")
btn1 = tk.Button(menu,text="Sabores",font=("Arial",18), #se muestra la seccion de sabores, con fuente arial y tamaño 18 de letra
command=lambda:mostrar(frame_sabores)) 
btn1.pack(side="left",expand=True,fill="x")
btn2 = tk.Button(menu,text="Tu pedido",font=("Arial",18), #se muestra la seccion de tu pedido, con fuente arial y tamaño 18 de letra
command=lambda:mostrar(frame_pedido))
btn2.pack(side="left",expand=True,fill="x")
btn3 = tk.Button(menu,text="Total",font=("Arial",18),#se muestra la seccion de total, con fuente arial y tamaño 18 de letra
command=lambda:mostrar(frame_total))
btn3.pack(side="left",expand=True,fill="x")
# ---------- CONTENEDOR ----------
contenedor = tk.Frame(ventana) #se guardan las secciones
contenedor.pack(fill="both", expand=True) #cada seccion es independiente
frame_sabores = tk.Frame(contenedor)
frame_pedido = tk.Frame(contenedor)
frame_total = tk.Frame(contenedor)

for frame in (frame_sabores, frame_pedido, frame_total): #hace que esten superpuestas las secciones
    frame.grid(row=0,column=0,sticky="nsew")
# ---------- SABORES ----------
titulo = tk.Label(frame_sabores,text="Sabores disponibles", #texto en pantalla
font=("Arial",26))
titulo.pack(pady=20)

for sabor in sabores: #recorre cada sabor
    boton = tk.Button( #botón creado
        frame_sabores,
        text=sabor,
        font=("Arial",20),
        width=15,
        command=lambda s=sabor:elegir_sabor(s)#se ejecuta 
    )
    boton.pack(pady=8)
    botones_sabores[sabor] = boton #se guarda en el diccionario para cambiar su color despues
# ---------- PEDIDO ----------
titulo_pedido = tk.Label(frame_pedido,text="Tu pedido", #texto en pantalla
font=("Arial",26))
titulo_pedido.pack(pady=20)
pedido_label = tk.Label(frame_pedido,text="",
font=("Arial",22))
pedido_label.pack()
# ---------- TOTAL ----------
titulo_total = tk.Label(frame_total,text="Total", #texto en pantalla
font=("Arial",26))
titulo_total.pack(pady=20)
precio_label = tk.Label(frame_total,text="$0", #muestra el precio
font=("Arial",30))
precio_label.pack(pady=20)
boton_confirmar = tk.Button(frame_total, #se confirma el pedido
text="Confirmar pedido",
font=("Arial",20),
command=confirmar)
boton_confirmar.pack(pady=10)
boton_reiniciar = tk.Button(frame_total, #se reinicia el pedido
text="Reiniciar",
font=("Arial",20),
command=reiniciar)
boton_reiniciar.pack(pady=10)
mostrar(frame_sabores) #cuando inicia el programa, muestra sabores
ventana.mainloop() #iniciar aplicación