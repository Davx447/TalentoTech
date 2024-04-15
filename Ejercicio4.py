class ejercicio4:

# Definimos cadena:
    cadena = "hola a todos, bienvenido a mi codigo jsjs."

# Método .capitalize(): Convierte la primera letra en mayúscula
    print("capitalize():", cadena.capitalize())

# Método .upper(): Convierte toda la cadena a mayúsculas
    print("upper():", cadena.upper())

# Método .lower(): Convierte toda la cadena a minúsculas
    print("lower():", cadena.lower())

# Método .title(): Convierte la primera letra de cada palabra en mayúscula
    print("title():", cadena.title())

# Método .count(): Cuenta el número de veces que aparece una subcadena
    print("count('o'):", cadena.count('o'))

# Método .find(): Devuelve el índice de la primera aparición de una subcadena
    print("find('mundo'):", cadena.find('mundo'))

# Método .split(): Divide la cadena en una lista de subcadenas
    print("split():", cadena.split())

# Método .join(): Une una lista de subcadenas en una sola cadena
    subcadenas = ['hola', 'mundo']
    print("join():", ' '.join(subcadenas))

# Método .strip(): Elimina espacios en blanco al principio y al final de la cadena
    cadena_con_espacios = "  hola mundo  "
    print("strip():", cadena_con_espacios.strip())

# Método .replace(): Reemplaza una subcadena por otra
    print("replace('mundo', 'universo'):", cadena.replace('mundo', 'universo'))

# Método .zfill(): Rellena la cadena con ceros a la izquierda hasta alcanzar una longitud específica
    numero = "42"
    print("zfill(5):", numero.zfill(5))
