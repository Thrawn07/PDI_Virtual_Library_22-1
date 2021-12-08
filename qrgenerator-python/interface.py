#librerias
from os import read
from tkinter import *
from tkinter import font, ttk
import sqlite3
#import qrcode
#import cv2


####   FUNCIONES PARA GENERAR CÓDIGOS QR    ####
"""
def codigol1():        
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("""#SELECT LINK FROM QR WHERE ID_QR=1""")
"""tupla = c.fetchall()
    s  = str(tupla[0][0:])
    print(type(s))
    print(s)
    conn.close()
    qr1 = qrcode.make(s)
    qr1.save('1.png')
    print("QR generado")"""


####    VENTANA ####
ventana=Tk() 
ventana.geometry("640x480")
ventana.title("BooQR")

####    LISTAS PARA COMBOBOXES   ####
listlibro1=[ "El arte de la guerra", "El criterio"]
listlibro2=["El tesoro de David"]
listlibro3=[ "El contrato social"]
listlibro4=["Gramática castellana"]
listlibro5=["El origen de las especies"]
listlibro6=["CSS avanzado"]
listlibro7=["Lenguaje musical II", "La divina comedia"]
listlibro8=["Alicia en el país de las Maravillas","Frankestein","Dagón","El gato negro","Don Quijote de la mancha",
"El sabueso de los Baskerville","'El lobo Estepario","Viaje al centro de la tierra","El fantasma de Canterville"]
listlibro9=["Historia de la revolución rusa"]

#Variables que almacenarán los datos
categoria = IntVar()
categoria.set(1)
 

#etiquetas

etiqueta = ttk.Label(ventana,text = "Bienvenidos! Seleccione el libro que desee: ", background="blue")
etiqueta.grid(row=1, column=1)
etiqueta_categoria =  ttk.Label(ventana, text='Categoria: ')
entrada_categoria_1 = ttk.Label(ventana, text='Filosofia y psicologia')
entrada_categoria_2 = ttk.Label(ventana, text='Lenguas',  )
entrada_categoria_3 = ttk.Label(ventana, text='Artes' )
entrada_categoria_4 = ttk.Label(ventana, text='Religion')
entrada_categoria_5 = ttk.Label(ventana, text='Ciencias naturales y matematicas')
entrada_categoria_6 = ttk.Label(ventana, text='Literatura y retorica')
entrada_categoria_7 = ttk.Label(ventana, text='Ciencias sociales')
entrada_categoria_8 = ttk.Label(ventana, text='Tecnologia')
entrada_categoria_9 = ttk.Label(ventana, text='Geografia e historia')
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



"""
def button_event():
    codigol1()
    Image.open('1.png')"""

    



        
















####    INSTANCIA   ####
button = Button(master=ventana,text="Obtener libro",width=120)
button.grid(row=11, column=2)


ventana.mainloop()