#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

archivo = open('/home/aliet/PythonIn/pythonInicial/prueba11','w+t')
#x para crear
#t para texto
archivo.write("Ejercicio 11 del módulo entrada y salida de datos")
archivo.close()

archivo = open('/home/aliet/PythonIn/pythonInicial/prueba11','rt')
leer = archivo.read()
print(leer)
archivo.close()
