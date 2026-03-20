import tkinter 
from tkinter import messagebox
bochas=[]
sabores=["crema","vainilla","chocolate","bacon caramelizado","carne de caballo","bondiola","barro chaqueño"]
precios_bocha=["$700","$1200","$1600"]
def click():
    


    a=tkinter.IntVar()     
    num_boch=["1 bocha","2 bocha","3 bocha"]        
    ventana = tkinter.Tk()
    root = tkinter.Tk()
    root.withdraw()
    ancho = root.winfo_screenwidth()
    alto  = root.winfo_screenheight()
    ventana.geometry(f"{ancho}x{alto}")
    ventana.title("heladeria")
    ventana.config(background="#2A9B5D") 

    ram= tkinter.Label(ventana, text="dulce dia",font=("Arial",35,"bold"),
                     relief="sunken",
                     bd=20)
    ram.pack()
    
    steve=tkinter.Label(ventana,text="cuantas bochas quiere?",font=("Arial",18,"bold"),background="#A8F3CA")
    steve.place(x=50,y=120)
    steve1=tkinter.Label(ventana,text="1 bocha",font=("Ariel",18,),background="#A8F3CA")
    steve1.place(x=50,y=170)
    steve2=tkinter.Label(ventana,text="2 bocha",font=("Ariel",18,),background="#A8F3CA")
    steve2.place(x=50,y=229)
    steve3=tkinter.Label(ventana,text="3 bocha",font=("Ariel",18),background="#A8F3CA")
    steve3.place(x=50,y=290)
    x_cord=173
    y_cord=135
    xx_cord=750
    yy_cord=100
    for index in range(len(num_boch)):
        salto =20
        radioButton=tkinter.Radiobutton(ventana, text=num_boch[index], variable=a, value=index)
        for i in num_boch:
            radioButton.place(x=x_cord, y=y_cord)
            y_cord+=salto
    
    for carl in range(len(sabores)):
        salto =7
        
        trunks=tkinter.Radiobutton(ventana, text=sabores[carl], variable=a, value=carl)
        for i in sabores:
            trunks.place(x=xx_cord, y=yy_cord)
            yy_cord+=salto
            
def holi():

    ventana = tkinter.Tk()
    root = tkinter.Tk()
    root.withdraw()
    ancho = root.winfo_screenwidth()
    alto  = root.winfo_screenheight()
    ventana.geometry(f"{ancho}x{alto}")
    ventana.title("heladeria")
    ventana.config(background="#2A9B5D") 

    ram = tkinter.Label(ventana, text="dulce dia",font=("Arial",35,"bold"),
                     relief="sunken",
                     bd=20)
    
#def recibo():
   

ventana = tkinter.Tk()

root = tkinter.Tk()
root.withdraw()
ancho = root.winfo_screenwidth()
alto  = root.winfo_screenheight()
ventana.geometry(f"{ancho}x{alto}")

ventana.title("heladeria")
ventana.config(background="#2A9B5D") 

juan = tkinter.Label(ventana, text="dulce dia",font=("Arial",35,"bold"),
                     relief="sunken",
                     bd=20)
juan.pack()
carlo=tkinter.Label(ventana,text="que le gustaria hoy?",font=("Arial",18,"bold"),background="#A8F3CA")
carlo.place(x=50,y=120)
tony=tkinter.Label(ventana,text="helado de a bocha",font=("Ariel",18,),background="#A8F3CA")
tony.place(x=50,y=160)
tony2=tkinter.Label(ventana,text="el kilo de helado",font=("Ariel",18,),background="#A8F3CA")
tony2.place(x=50,y=200)
tony3=tkinter.Label(ventana,text="finalizar compra o no compre nada",font=("Ariel",18),background="#A8F3CA")
tony3.place(x=50,y=240)
boton= tkinter.Button(ventana,text="click", command=click, bg="#A8F3CA")
boton.place(x=260,y=165)
horton= tkinter.Button(ventana,text="click", command=holi, bg="#A8F3CA")
horton.place(x=255,y=205)



ventana.mainloop()

