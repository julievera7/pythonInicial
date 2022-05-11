#Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

def main():
	num = int(input("Cuántos países va a introducir: "))
	pais = []
	for i in range(num):
		nombre = input(f"Introduzca el país {i+ 1}: ")
		pais += [nombre]
	print(f"Los países son: {pais}")
	
	listapais = set(pais)
	ordenada = sorted(listapais, reverse=False)
	print(ordenada)

if __name__ == "__main__":
	main()
