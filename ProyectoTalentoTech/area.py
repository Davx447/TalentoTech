class Area:

    """---------------------
    #Atributos
    ----------------------"""
    
    nombre=""
    Descripcion=""
    ListaEmpealodsArea=[]

    """--------------------------
    #Metodos
    ---------------------------"""

    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.Descripcion = descripcion
        self.ListaEmpleadosArea = []

    def agregar_empleado(self, empleado):
        self.ListaEmpleadosArea.append(empleado)
