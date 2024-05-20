from empleado import Empleado

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

    def cuantosEmpleadosTieneElJefe(self, pJefe):
        count = 0
        for empleado in self.empleados:
            if empleado.jefe == pJefe:
                count += 1
        return count
    
    def empleadosACargoDelJefe(self, pJefe):
        empleadosACargo = []
        for empleado in self.empleados:
            if empleado.jefe == pJefe:
                empleadosACargo.append(empleado)
        return empleadosACargo
