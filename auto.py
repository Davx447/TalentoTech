class Auto:
    """Clase que representa un auto"""
    
    def __init__(self, modelo, marca, color):
        """inicializa los atributos del auto"""
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.kilometraje = 0
        
    def describir_auto(self):
        """Imprime informacion sobre el auto."""
        print(f"Auto {self.modelo} - Marca: {self.marca} - Color: {self.color}")
        
    def leer_kilometraje(self):
        """Imprime el kilometraje del auto"""
        print(f"El kilometraje del auto es: {self.kilometraje} km")
        
    def actualizar_kilometraje(self, kilometraje):
        """
        Actualiza el atributo de kilometraje del auto.
        No permite retroceder el kilometraje
        """
        if kilometraje >= self.kilometraje:
            self.kilometraje = kilometraje
        else:
            print("No se puede retroceder el kilometraje.")
            
            
class AutoElectrico(Auto):
    """Clase que representa un auto electrico, heredada de Auto."""
    
    def __init__(self, modelo, marca, color, capacidad_bateria):
        """Inicializa los atributos de un auto electrico."""
        super().__init__(modelo, marca, color)
        self.capacidad_bateria = capacidad_bateria
        
    def describir_auto_electrico(self):
        """Imprime informacion especifica sobre el auto electrico."""
        print(f"Auto electrico {self.modelo} - Marca: {self.marca} - Color: {self.color}")
        print(f"Capacidad de la bateria: {self.capacidad_bateria} kwh")
        

# Crear una instancia de auto y llamar a sus metodos
mi_auto = Auto("Civic", "Honda", "Rojo")
mi_auto.describir_auto()
mi_auto.actualizar_kilometraje(15000)
mi_auto.leer_kilometraje()
    
# Crear una instancia de Autoelectrico y llamar a sus metodos
mi_auto_electrico = AutoElectrico("Model S", "Tesla", "Blanco", 100)
mi_auto_electrico.describir_auto_electrico()
mi_auto_electrico.actualizar_kilometraje(5000)
mi_auto_electrico.leer_kilometraje()
