#Crear una lista
numeros = [1, 2, 3, 4, 5]

#Crear un diccionario de nombres y edades
personas = {
    "Juan " : 30,
    "Maria " : 25,
    "Pedro" : 28,
}

# Guardar la lista en un archivo CSV
with open("numeros.csv", "W") as archivo_csv:
    for numero in numeros:
        archivo_csv.write(f'{numero}\n')
        
# Guardar el diccionario en un archivo CSV
with open("personas.txt", "W") as archivo_txt:
    for nombre, edad in personas.items():
        archivo_txt.write(f'{nombre}: {edad}\n')
        
    print("Listo, los datos se han guardado en archivos 'numeros.csv' y 'personas.txt'")
