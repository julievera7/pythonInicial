#Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.

#altura = input("Ingrese la altura del triangulo (cm): ")
#base = input ("Ingrese la base del triangulo (cm): ") 
import math 

def areatriangulo(altura, base):
	return (altura*base)/2
	
print("El área del triangulo es: ", areatriangulo(int(input("Ingrese la altura del triangulo (cm): ")), int(input ("Ingrese la base del triangulo (cm): "))  ))

def areacirculo(radio):
	return (math.pi * radio * radio)
	
print("El área del círculo es: ", areacirculo(int(input("Ingrese el radio del círculo: "))))	
