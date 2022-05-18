#En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido de tipo texto.
#Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
#Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

import sqlite3
#Realizar búsqueda por nombre

datos = sqlite3.connect("ejercicio17.bd")
cursor = datos.cursor()

nombre = str(input("Ingrese el nombre: "))
cursor = datos.execute("SELECT id, nombre, apellido FROM alumnos WHERE nombre=?", (nombre, ))
row=cursor.fetchall()

if row!=None:
    print(row)
else:
    print("No está registrado en la base de datos")
cursor.close()
datos.close()
    
#Imprimir todos los datos
#datos = sqlite3.connect('ejercicio17.bd')
#cursor = datos.cursor()
#rows = cursor.execute('SELECT * FROM alumnos')

#for row in rows:
#    print(row)  

#cursor.close()
#datos.close()



