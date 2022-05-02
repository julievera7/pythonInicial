#Escribe una función que pueda decirte si un número (número entero) es primo o no.

def primo(numero):

	if numero == 2 or numero == 1:
		return "Es primo"
	for i in range(2,numero,1):
		if numero % i == 0:
			return "No es primo"
		else:
			return "Es primo"
print(primo(int(input("Introduzca un número: "))))
