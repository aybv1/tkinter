import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import ttk, messagebox

ventana = tk.Tk() # Instanciar ventana principal
ventana. title("Saludo interactivo")
ventana. geometry("363x180")

def saludar(): #Función invocada cuando se hace clic
    nombre = entrada.get().strip() # Leer y quitar espacios
   
    if not nombre: # Comprobar que exista un nombre
        messagebox.showwarning("Dato requerido", "Ingrese su nombre") #Si esta vaicio, envia alerta de advertencia

        return
    #Nombre valido, muestra el mensaje
    messagebox.showinfo("Saludo",f"¡Hola, {nombre}!")


ttk. Label(ventana, text="Nombre:").pack(pady=(16, 4)) # Etiqueta para el campo de entrada
entrada = ttk. Entry(ventana) # Campo de una linea
entrada.pack(padx=20, fill="x") # Empaquetar con relleno horizontal y margen lateral
ttk.Button(ventana, text="Saludar", command=saludar).pack(pady=12) # Boton que invoca la funcion saludar al hacer
ventana.mainloop() # Ejecutar interfaz