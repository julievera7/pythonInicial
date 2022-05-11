#En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
import pickle

class Vehiculo:
	def __init__(self, marca, rueda):
		self.marca = marca
		self.rueda = rueda

	def getMarca(self):
		return self.marca

carro = Vehiculo("Ford",4)
#print(carro.getMarca())

archivo = open('datos.bin','wb')
pickle.dump(carro, archivo)
archivo.close()

archivo = open('datos.bin','rb')
carro = pickle.load(archivo)
archivo.close()

print(type(carro))
print(carro.getMarca())
