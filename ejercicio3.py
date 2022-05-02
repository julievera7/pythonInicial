#Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.

numeros = [1]



for num in numeros:
	numeros.append(num + 1)
	if num == 99:
		break
print(numeros)
print("Números en orden inverso")
print(sorted(numeros, reverse=True))
