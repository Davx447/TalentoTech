import csv

def cargar_datos(self, archivo_empleados, archivo_jefes, archivo_areas):
    with open(archivo_empleados, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Saltar la primera fila que contiene los encabezados
        for row in reader:
            if len(row) < 6:
                continue  # Ignorar filas incompletas
            empleado = Empleado(row[0], row[1], int(row[2]), float(row[3]), row[4], row[5])
            self.empleados.append(empleado)

    with open(archivo_jefes, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Saltar la primera fila que contiene los encabezados
        for row in reader:
            if len(row) < 6:
                continue  # Ignorar filas incompletas
            jefe = Jefe(row[0], row[1], int(row[2]), float(row[3]), row[4], row[5])
            self.jefes.append(jefe)
            if len(row) > 6 and row[6]:
                empleados_a_cargo = row[6].split(', ')
                for emp_nombre in empleados_a_cargo:
                    for emp in self.empleados:
                        if emp.obtener_nombre_completo() == emp_nombre:
                            jefe.agregar_empleado(emp)

    with open(archivo_areas, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Saltar la primera fila que contiene los encabezados
        for row in reader:
            if len(row) < 3:
                continue  # Ignorar filas incompletas
            area = Area(row[0], row[1])
            self.areas.append(area)
            if row[2]:
                empleados_area = row[2].split(', ')
                for emp_nombre in empleados_area:
                    for emp in self.empleados:
                        if emp.obtener_nombre_completo() == emp_nombre:
                            area.agregar_empleado(emp)
