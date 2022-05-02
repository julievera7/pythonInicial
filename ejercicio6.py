#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def bisiestro(year):
	if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0 ):
		return "Es bisiestro"
	return"No es bisiestro"
print(bisiestro(int(input("Introduzca el año: "))))
