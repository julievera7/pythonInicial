
# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
	#Metodo para inicializar
	def __init__(self, nombre, calificacion):
		self.nombre = nombre
		self.calificacion = calificacion
	#Metodo para imprimir
	def __str__(self):
		return "Nombre del alumno: {} \nCalificación: {}".format(self.nombre, self.calificacion)
	
	#Metodo para mostrar mensaje
	def mensaje(self):
		if self.calificacion >=10:
			print("Aprobado")
		else:
	  		print("Reprobado")

estudiante = Alumno("Juan", 10)
print(estudiante)
estudiante.mensaje()
