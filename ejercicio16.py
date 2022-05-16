#Ejercicio 2: En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.

import tkinter


window = tkinter.Tk()

label_title = tkinter.Label(window,text="Ejercicio 16")
label_title.pack()


label_texto = tkinter.Label(window,
                            text="crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label")

label_texto.pack(ipadx=10,ipady=10, expand=True)

lista = ["Mérida", "Caracas", "Nueva Exparta", "Bolívar", "Carabobo", "Maracay"]

lista_items = tkinter.StringVar(value=lista)

listbox = tkinter.Listbox(window,
                          height=3,
                          listvariable=lista_items,
                          selectmode='extended',
                          #yscrollcommand = True
                          )
scrollbar = tkinter.Scrollbar(window,
                              orient='vertical',
                              command=listbox.yview
                              )
listbox['yscrollcommand'] = scrollbar.set
listbox.pack(ipadx=10,ipady=10, expand=True)
window.mainloop()
