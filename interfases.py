# import pprint
import tkinter
from tkinter import ttk

window = tkinter.Tk()

# print(type(window))
# pprint.pprint(dir(window))

#  Geometrias
# Widgets
# label

# label_saludo = tkinter.Label(window, text="Hola", bg="green", fg="black")
# label_saludo.pack(ipadx=50, ipady=50, side='left')

# label_adios = tkinter.Label(window, text="Adios", bg="red", fg="black")
# label_adios.pack(ipadx=50, ipady=50, side='right')

# GRID

# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=3)

# username_label = ttk.Label(window, text="username:")
# username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

# username_entry = ttk.Entry(window)
# username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

# password_label = ttk.Label(window, text="password:")
# password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

# password_entry = ttk.Entry(window, show='*')
# password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

# # Button
# login_button = ttk.Button(window, text='Login')
# login_button.grid(column=1, row=3, sticky=tkinter.E, padx=5, pady=5)

#  place

label1 = tkinter.Label(
    window, text='posicionamiento absoluto', bg='black', fg='white')
label1.place(x=10, y=50)

label2 = tkinter.Label(window, text='otro mas', bg='red', fg='yellow')
label2.place(x=25, y=40)


window.mainloop()
