from empleado import Empleado

class Area:

    """---------------------
    #Atributos
    ----------------------"""
    
    nombre=""
    Descripcion=""
    ListaEmpleadosArea=[]

    """--------------------------
    #Metodos
    ---------------------------"""

    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.Descripcion = descripcion
        self.ListaEmpleadosArea = []
        
    def agregar_empleado(self, empleado):
        self.ListaEmpleadosArea.append(empleado)

    def cuantosEmpleadosEnArea(self, pAreaY):
    
        count = 0
        for empleado in self.empleados:
            if empleado.area == pAreaY:
                count += 1
        return count
    
    def cuantosEmpleadosEnArea(self, pAreaX):
        count = 0
        for empleado in self.empleados:
            if empleado.area == pAreaX:
                count += 1
        return count
