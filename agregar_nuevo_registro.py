import csv

# Definir el nuevo registro
nuevo_registro = {'nombre': 'Pedro', 'edad': 35}
                  
#Abrir el archivo CSV en modo de escritura(a+ para añadir al final)
with open('numeros.csv', mode='a+', newline='') as archivo:
    #Crear el escritor CSV
    escritor_csv = csv.DictWriter(archivo, fieldnames=['nombre', 'edad'])
    
    #Verificar si el archivo esta vacio (para agregar los encabezados si es necesario)
    archivo.seek(0)
    primer_caracter = archivo.read(1)
    if not primer_caracter:
        escritor_csv.writeheader()
        
    #Agregar el nuevo registro al archivo CSV
    escritor_csv.writerow(nuevo_registro)
