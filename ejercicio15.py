#Ejercicio 1: En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado
# y que contenga un botón de reinicio para que deje todo como al principio.
#  Al principio no tiene que haber una opción seleccionada.

import tkinter
from tkinter import ttk

   

window = tkinter.Tk()

def reboot():
   seleccion.set(None)


window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)

label_titulo = ttk.Label(window, text="Ejercicio 15: Lista de RadioButton")
label_titulo.grid(column=0, row=0, sticky=tkinter.W)


seleccion = tkinter.StringVar()
r1 = ttk.Radiobutton(window,
                             text="EEUU",
                             value='1',
                             variable=seleccion)
r2 = ttk.Radiobutton(window,
                             text="Venezuela",
                             value='2',
                             variable=seleccion)
r3 = ttk.Radiobutton(window,
                             text="Alemania",
                             value='3',
                             variable=seleccion)

r1.grid(column=0, row=1, pady=5, padx=5)
r2.grid(column=0, row=2, pady=5, padx=5)
r3.grid(column=0, row=3, pady=5, padx=5)

#boton
reboot_button = ttk.Button(window, text="Reiniciar", command=reboot)
reboot_button.grid(column=1, row=4, sticky=tkinter.E, padx=5, pady=5)
window.mainloop()
