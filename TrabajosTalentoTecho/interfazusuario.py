import tkinter as tk

def agregarEstudiante():
    nombre= nombre_entry.get()
    edad=int(edad_entry.get())
    carrera= carrera_entry.get()

    with open ("estudiante.txt", "a") as archivo:
        archivo.write(f"{nombre, {edad}, {carrera}\n")
                         
nombre_entry.delete(0, tkEND)
edad_entry.delete(0, tkEND)
carrera_entry.delete(0, tkEND)
