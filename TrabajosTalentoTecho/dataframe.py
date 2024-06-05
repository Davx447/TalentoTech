import pandas as pd

#Crear un diccionario con los datos
datos= {
    "Juan " : 30,
    "Maria " : 25,
    "Pedro" : 28,
}

# Crear el Data Frame
df= pd.DataFrame(datos)

#Guardar el DataFrame en un archivo CSV
df.to_csv('datos.csv', index=False)
    
