class Jefe:

    """---------------------
    #Atributos
    ----------------------"""

    empleadosACargo=[]

    """--------------------------
    #Metodos
    ---------------------------"""

    def __init__(self, empleadosACargo ):
        self.empleadosACargo = empleadosACargo

    def agregar_empleado(self, empleado):
        self.empleadosACargo.append(empleado)
