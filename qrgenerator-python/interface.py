from tkinter import*
from tkinter import font
from tkinter import messagebox

ventana =Tk()
ventana.geometry("600x600")
ventana.title("Procesamiento digital de imagenes")
#Variables que almacenarán los datos
genero = IntVar()
genero.set(1)
libro = StringVar()
libro.set("seleccione opcion")

etiqueta = Label(ventana,text = "Bienvenidos seleccione el libro que desee: ", bg = "blue")
etiqueta.grid(row=1, column=2)
#####definicion de variable y boton
def Despedida():
   messagebox.showinfo("Welcome to GFG.",  "Hasta Luego")

#boton1=Button(ventana, text ="press it", command= Despedida)
#boton1.grid(row=8, column=3)
etiqueta_genero = Label(ventana, text='Genero: ')
entrada_genero_1 = Radiobutton(ventana, text='Filosofia y psicologia', variable=genero, value=1)
entrada_genero_2 = Radiobutton(ventana, text='Lenguas', variable=genero, value=2)
entrada_genero_3 = Radiobutton(ventana, text='Artes', variable=genero, value=3)
entrada_genero_4 = Radiobutton(ventana, text='Religion', variable=genero, value=4)
entrada_genero_5 = Radiobutton(ventana, text='Ciencias naturales y matematicas', variable=genero, value=5)
entrada_genero_6 = Radiobutton(ventana, text='Literatura y retorica', variable=genero, value=6)
entrada_genero_7 = Radiobutton(ventana, text='Ciencias sociales', variable=genero, value=7)
entrada_genero_8 = Radiobutton(ventana, text='Tecnologia', variable=genero, value=8)
entrada_genero_9 = Radiobutton(ventana, text='Geografia e historia', variable=genero, value=9)
#placement of buttons 
entrada_genero_1.grid(row=2, column=1)
entrada_genero_2.grid(row=3, column=1)
entrada_genero_3.grid(row=4, column=1)
entrada_genero_4.grid(row=5, column=1)
entrada_genero_5.grid(row=6, column=1)
entrada_genero_6.grid(row=7, column=1)
entrada_genero_7.grid(row=8, column=1)
entrada_genero_8.grid(row=9, column=1)
entrada_genero_9.grid(row=10, column=1)
#entrada de las listas
entrada_libro_1= OptionMenu(ventana, libro, "El arte de la guerra", "El criterio", "Activo")
entrada_libro_2= OptionMenu(ventana, libro, "El arte de la guerra", "El criterio", "Activo")
entrada_libro_3= OptionMenu(ventana, libro, "El arte de la guerra", "El criterio", "Activo")
entrada_libro_4= OptionMenu(ventana, libro, "El arte de la guerra", "El criterio", "Activo")
entrada_libro_5= OptionMenu(ventana, libro, "El arte de la guerra", "El criterio", "Activo")
entrada_libro_6= OptionMenu(ventana, libro, "El arte de la guerra", "El criterio", "Activo")
entrada_libro_7= OptionMenu(ventana, libro, "El arte de la guerra", "El criterio", "Activo")
entrada_libro_8= OptionMenu(ventana, libro, "El arte de la guerra", "El criterio", "Activo")
entrada_libro_9= OptionMenu(ventana, libro, "El arte de la guerra", "El criterio", "Activo")




#mostrar las listas 
entrada_libro_1.grid(row=2, column=2)
entrada_libro_2.grid(row=3, column=2)
entrada_libro_3.grid(row=4, column=2)
entrada_libro_4.grid(row=5, column=2)
entrada_libro_5.grid(row=6, column=2)
entrada_libro_6.grid(row=7, column=2)
entrada_libro_7.grid(row=8, column=2)
entrada_libro_8.grid(row=9, column=2)
entrada_libro_9.grid(row=10, column=2)



ventana.mainloop()