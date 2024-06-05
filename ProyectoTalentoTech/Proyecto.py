import csv

class Empleado:

    """---------------------
    #Atributos
    ----------------------"""

    nombre=""
    apellido=""
    edad=0
    salario=0
    dni=0
    fecha_vinculacion=""

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
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}, Edad: {self.edad}, Salario: {self.salario}, DNI: {self.dni}, Fecha de Vinculación: {self.fecha_vinculacion}"

class Jefe:

    """---------------------
    #Atributos
    ----------------------"""

    empleadosACargo=[]

    """--------------------------
    #Metodos
    ---------------------------"""

    def __init__(self, nombre, apellido, edad, salario, dni, fecha_vinculacion):
            super().__init__(nombre, apellido, edad, salario, dni, fecha_vinculacion)
            self.empleadosACargo = []

    def agregar_empleado(self, empleado):
        self.empleadosACargo.append(empleado)

    def listar_empleados_a_cargo(self):
        return [empleado.obtener_nombre_completo() for empleado in self.empleados_a_cargo]

    def __str__(self):
        return f"{super().__str__()}, Empleados a Cargo: {', '.join(self.listar_empleados_a_cargo())}"

class Area:

    """---------------------
    #Atributos
    ----------------------"""
    
    nombre=""
    Descripcion=""
    empleados=[]

    """--------------------------
    #Metodos
    ---------------------------"""

    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.Descripcion = descripcion
        self.empleados = []
        
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def listar_empleados(self):
        return [empleado.obtener_nombre_completo() for empleado in self.empleados]

    def __str__(self):
        return f"Área: {self.nombre}, Descripción: {self.descripcion}, Empleados: {', '.join(self.listar_empleados())}"

class SistemaGestionEmpleados:
    def __init__(self):
        self.empleados = []
        self.jefes = []
        self.areas = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def eliminar_empleado(self, dni):
        self.empleados = [empleado for empleado in self.empleados if empleado.dni != dni]
    
    def modificar_empleado(self, dni, nombre=None, apellido=None, edad=None, salario=None, fecha_vinculacion=None):
        for empleado in self.empleados:
            if empleado.dni == dni:
                if nombre:
                    empleado.nombre = nombre
                if apellido:
                    empleado.apellido = apellido
                if edad:
                    empleado.edad = edad
                if salario:
                    empleado.salario = salario
                if fecha_vinculacion:
                    empleado.fecha_vinculacion = fecha_vinculacion

    def mostrar_empleado(self, dni):
        for empleado in self.empleados:
            if empleado.dni == dni:
                return str(empleado)
        return "Empleado no encontrado"
    
def agregar_jefe(self, jefe):
        self.jefes.append(jefe)

def eliminar_jefe(self, dni):
        self.jefes = [jefe for jefe in self.jefes if jefe.dni != dni]

def modificar_jefe(self, dni, nombre=None, apellido=None, edad=None, salario=None, fecha_vinculacion=None):
        for jefe in self.jefes:
            if jefe.dni == dni:
                if nombre:
                    jefe.nombre = nombre
                if apellido:
                    jefe.apellido = apellido
                if edad:
                    jefe.edad = edad
                if salario:
                    jefe.salario = salario
                if fecha_vinculacion:
                    jefe.fecha_vinculacion = fecha_vinculacion

def mostrar_jefe(self, dni):
        for jefe in self.jefes:
            if jefe.dni == dni:
                return str(jefe)
        return "Jefe no encontrado"

def agregar_area(self, area):
        self.areas.append(area)

def eliminar_area(self, nombre):
        self.areas = [area for area in self.areas if area.nombre != nombre]

def modificar_area(self, nombre, nuevo_nombre=None, descripcion=None):
        for area in self.areas:
            if area.nombre == nombre:
                if nuevo_nombre:
                    area.nombre = nuevo_nombre
                if descripcion:
                    area.descripcion = descripcion

def mostrar_area(self, nombre):
        for area in self.areas:
            if area.nombre == nombre:
                return str(area)
        return "Área no encontrada"

#Metodos para responder preguntas planteadas
def quienEsJefeDeEmpleado(self, pEmpleado):
        for empleado in self.empleados:
            if empleado == pEmpleado:
                return empleado.jefe
        return "Empleado no tiene jefe asignado"
    
def AreaEmpleado(self, pEmpleado):

        for empleado in self.empleados:
            if empleado == pEmpleado:
                return empleado.area
        return "Empleado no está asignado a ninguna área"

def contar_empleados_en_area(self, nombre_area):
    for area in self.areas:
        if area.nombre == nombre_area:
            return len(area.empleados)
    return 0

def listar_empleados_en_area(self, nombre_area):
    for area in self.areas:
        if area.nombre == nombre_area:
            return area.obtener_empleados()
    return []

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

def ConsultarSalario(self, pEmpleado):
        for empleado in self.empleados:
            if empleado == pEmpleado:
                return empleado.salario
        return None
