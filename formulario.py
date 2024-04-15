import tkinter as tk
from tkinter import messagebox
import csv

def guardar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    
    #Verificar sis e ingresaron todos los campos
    if nombre == '' or edad == '':
        messagebox.showerror('Error', 'Por favor, ingresa todos los campos')
        return
    
    #Guardar los datos en un archivo CSV
    with open('datos.csv', 'a', newline ='') as file:
        writer = csv.writer(file)
        writer.writerow([nombre, edad])
        
    messagebox.showinfo('Exito', 'Los datos se han guardado correctamente')
    
#Crear la ventana principal
ventana = tk.Tk()
ventana.title('Formulario')

#Crear etiquetas y campos de entrada
tk.Label(ventana, text='Nombre:').grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry/(ventana)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(ventana, text='Edad:').grid(row=1, column=0, padx=5, pady=5)
entry_edad = tk.Entry/(ventana)
entry_edad.grid(row=1, column=1, padx=5, pady=5)

# Boton para guardar los datos
tk.Button(ventana, text='Guardar', command=guardar_datos).grid(row=2, columnspan=2, padx=5, pady=5)

#Ejecutar aplicacion
ventana.mainloop()
