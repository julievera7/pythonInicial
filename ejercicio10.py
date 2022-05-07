# En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

# En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el tiempo que queda de trabajo.

import time
hora =  time.strftime("%H", time.localtime())
minutos = time.strftime("%M", time.localtime())

	

print('time():', time.ctime(time.time()), 
      '\nlocaltime():', time.localtime())
if hora >= '19':
	print("Es hora de ir a casa")
else:
	resultadoh = 19-int(hora)
	resultadom = 60 - int(minutos)
	print("Debe trabajar por: ", resultadoh, "Horas", resultadom, "Minutos")
