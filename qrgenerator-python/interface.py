import tkinter

ventana = tkinter.Tk()
ventana.geometry("600x600")

etiqueta = tkinter.Label(ventana,text = "Bienvenidos a la biblioteca", bg = "red")
etiqueta.pack(fill = tkinter.X)
ventana.mainloop()




