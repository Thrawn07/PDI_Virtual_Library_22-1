#librerias
from tkinter import *
from tkinter import font, ttk
import customtkinter
import sqlite3
import qrcode

#prueba de tema  habilita el cambio de color de la interface con el sistema
customtkinter.enable_macos_darkmode()
customtkinter.set_appearance_mode("System")

#variables
ventana=Tk() 
ventana.geometry("500x350")
ventana.title("Procesamiento digital de imagenes")
listlibro1=[ "El arte de la guerra", "El criterio", "Activo"]
listlibro2=["El tesoro de David"]
listlibro3=[ "El contrato social"]
listlibro4=["Gramática castellana"]
listlibro5=["EL origen de las especie"]
listlibro6=["CSS avanzado","La Divina comedia"]
listlibro7=["Lenguaje musical II"]
listlibro8=["Alicia en el país de las Maravillas","Frankestein","Dagón","El gato negro","Don Quijote de la mancha",
"El sabueso de los Baskerville","'El lobo Estepario","Viaje al centro de la tierra","El fantasma de Canterville"]
listlibro9=["no available"]
#Variables que almacenarán los datos
categoria = IntVar()
categoria.set(1)
 

#etiquetas
etiqueta = Label(ventana,text = "Bienvenidos! Seleccione el libro que desee: ", bg = "blue")
etiqueta.grid(row=1, column=1)
etiqueta_categoria = Label(ventana, text='categoria: ')
entrada_categoria_1 = Radiobutton(ventana, text='Filosofia y psicologia', variable=categoria, value=1)
entrada_categoria_2 = Radiobutton(ventana, text='Lenguas', variable=categoria, value=2)
entrada_categoria_3 = Radiobutton(ventana, text='Artes', variable=categoria, value=3)
entrada_categoria_4 = Radiobutton(ventana, text='Religion', variable=categoria, value=4)
entrada_categoria_5 = Radiobutton(ventana, text='Ciencias naturales y matematicas', variable=categoria, value=5)
entrada_categoria_6 = Radiobutton(ventana, text='Literatura y retorica', variable=categoria, value=6)
entrada_categoria_7 = Radiobutton(ventana, text='Ciencias sociales', variable=categoria, value=7)
entrada_categoria_8 = Radiobutton(ventana, text='Tecnologia', variable=categoria, value=8)
entrada_categoria_9 = Radiobutton(ventana, text='Geografia e historia', variable=categoria, value=9)
#placement of buttons 
entrada_categoria_1.grid(row=2, column=1)
entrada_categoria_2.grid(row=3, column=1)
entrada_categoria_3.grid(row=4, column=1)
entrada_categoria_4.grid(row=5, column=1)
entrada_categoria_5.grid(row=6, column=1)
entrada_categoria_6.grid(row=7, column=1)
entrada_categoria_7.grid(row=8, column=1)
entrada_categoria_8.grid(row=9, column=1)
entrada_categoria_9.grid(row=10, column=1)
#entrada de las listas
entrada_libro_1= ttk.Combobox(ventana,values=listlibro1)
entrada_libro_2= ttk.Combobox(ventana,values=listlibro2)
entrada_libro_3= ttk.Combobox(ventana, values=listlibro3)
entrada_libro_4= ttk.Combobox(ventana,values=listlibro4)
entrada_libro_5= ttk.Combobox(ventana, values=listlibro5)
entrada_libro_6= ttk.Combobox(ventana,values=listlibro6)
entrada_libro_7= ttk.Combobox(ventana, values=listlibro7)
entrada_libro_8= ttk.Combobox(ventana,values=listlibro8)
entrada_libro_9= ttk.Combobox(ventana, values=listlibro9)


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




#######################################################################
                        ####    BOTÓN   ####
####    FUNCIÓN  ####
def button_event():
    print("button pressed")
















####    INSTANCIA   ####
button = customtkinter.CTkButton(master=ventana,text="Seleccionar libro",
command=button_event,width=120,height=32,border_width=0, corner_radius=8)
button.grid(row=11, column=2)


ventana.mainloop()