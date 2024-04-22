class perro:
	"""Clase que representa a un perro."""

	def _init_(self, nombre, edad):

			self.nombre = nombre
			self.edad = edad

	def sentarse(self):
		"""Simula el comportamiento de un perro sentandose."""
		print(f"{self.nombre} está sentado.")

	def dar_vuelta(self):
			"""Simula el comportamiento de un perro dando vueltas."""
			print(f"{self.nombre} está dando vueltas.")

# Definir instancias
# Crear  una instancia de Perro
mi_perro = perro("Fido", 6)

# Imprimir el nombre actual del perro
print(f"El nombre de mi perro es {mi_perro.nombre}")

tu_perro = perro("Firulais", 3)
print(f"El nombre de tu perro es {tu_perro.nombre}")

#Llamar a los metodos para simular comportamientos

mi_perro.sentarse()
mi_perro.dar_vuelta()
tu_perro.sentarse()
tu_perro.dar_vuelta()

# Cambiar el nombre del perro
mi_perro.nombre = 'Max'

# Imprimir el nuevo nombre del perro
print(f"El nuevo nombre de mi perro es {mi_perro.nombre}")
