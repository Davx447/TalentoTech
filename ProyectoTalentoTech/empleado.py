class Empleado:

    """---------------------
    #Atributos
    ----------------------"""

    nombre=""
    apellido=""
    edad=0
    salario=0
    dni=0
    fecha_inculacion=""

    """--------------------------
    #Metodos
    ---------------------------"""

    def __init__(self, nombre, apellido, edad, salario, dni, fecha_vinculacion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.salario = salario
        self.dni = dni
        self.fecha_inculacion = fecha_vinculacion

    def ObtenerNombreCompleto(self):
        return self.nombre +" "+ self.apellido
