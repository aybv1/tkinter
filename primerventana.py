import tkinter as tk    #Importa la libreria tkinter
from tkinter import ttk #Importa ttk para widges (elementos)

#Crear la ventana principal
ventana=tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("400x250")
ventana.resizable(True, True) # Permitir cambiar el ancho, no el alto

#Inicia la ventana
ventana.mainloop() # Atender clics y redibujados hasta cerrar 




#El programa arranca sin componentes, 
#Mostrando una ventana vacia

#Al no tener etiquetas ni botones dentro del bloque, la interfaz se genera vacia
