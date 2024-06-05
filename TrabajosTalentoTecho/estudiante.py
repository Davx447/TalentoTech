class Estudiante:
    # ATributos
    Nombre="Nombre"
    Edad=0
    Carrera="Carrera"
    # Metodos

    def __init__(self, Nombre, Edad, Carrera):
        self.nombre=Nombre
        self.edad=Edad
        self.carrera=Carrera

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Carrera:", self.carrera)

    def agregarEstudiante():
        nombre= input("Ingrese el nombre del estudiante: ")
        edad= int(input("Ingrese la edad del estudiante: "))
        carrera= input("Ingrese la carrera del estudiante" )
        with open("estudiantes.txt", "0") as archivo:
            archivo.write(f"{nombre}, {edad}, {carrera}\n")

    def leerEstudiante(partes):
        with open("estudiantes.txt", "0") as archivo:
            lineas = archivo.readlines()
            for linea in lineas :
                partes = linea.strip().split
            
        
    
