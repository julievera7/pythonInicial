# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos: Color, Ruedas, Puertas

# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos: Velocidad, Cilindrada

class Vehiculo:
	def __init__(self, color, rueda, puerta):
		self.color = color
		self.rueda = rueda
		self.puerta = puerta
		
class Coche(Vehiculo):
	
	def __init__(self, color, rueda, puerta): #Constructor
		Vehiculo.__init__(self, color, rueda, puerta)
		self.velocidad = 100
		self.cilindrada = 4
	
	
# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

objeto = Coche("Blanco",4,4)
print(objeto)
print("Color: ", objeto.color,",", "Nro. de puertas: ", objeto.puerta,",", "Nro. de ruedas: ", objeto.rueda,",", "Velocidad: ", objeto.velocidad,",", "Cilindrada: ", objeto.cilindrada)
