import csv
def guardar_datos(self, archivo_empleados, archivo_jefes, archivo_areas):
    with open(archivo_empleados, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Nombre', 'Apellido', 'Edad', 'Salario', 'DNI', 'Fecha de Vinculación'])
        for empleado in self.empleados:
            writer.writerow([empleado.nombre, empleado.apellido, empleado.edad, empleado.salario, empleado.dni, empleado.fecha_vinculacion])

    with open(archivo_jefes, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Nombre', 'Apellido', 'Edad', 'Salario', 'DNI', 'Fecha de Vinculación', 'Empleados a Cargo'])
        for jefe in self.jefes:
            writer.writerow([jefe.nombre, jefe.apellido, jefe.edad, jefe.salario, jefe.dni, jefe.fecha_vinculacion, ', '.join(jefe.listar_empleados_a_cargo())])

    with open(archivo_areas, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Nombre Área', 'Descripción', 'Empleados'])
        for area in self.areas:
            writer.writerow([area.nombre, area.descripcion, ', '.join(area.listar_empleados())])
