import random
from tkinter import *

dicti= 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM1234567890-_!¡@#$¢%&/÷=?¿+*^[]çÇ'
#passw = ""


# for i in range(0,16):
# 	value =  random.randint(1, (len(dicti)-1))
# 	passw = passw + dicti[value]
# 	print(passw)

# print(passw)

def generar_pass():
	for i in range(0,16):
		passw = ""
		value =  random.randint(1, (len(dicti)-1))
		passw = passw + dicti[value]
		espaciopass.insert(0, passw)

def reinicio():
	passw = ""

	espaciopass.delete(0, END)


root = Tk()
root.title("Password generator")
master = Frame(root)
master.config(padx = 50, pady = 50)
master.pack()
titulo = Label(master, text = "Mi primer generador de contraseñas", font = ("verdana", 20))
titulo.pack()
texto1 = Label(master, text = "\nHola, bienvenido al generador de contraseñas que estoy haciendo.\nEste programa generará una contraseña de 16 caracteres.\nPuedes duplicar su longidud pulsando dos veces sobre el botón.\n")
texto1.pack()
espaciopass = Entry(master, width = 35, font = ("verdana", 18), justify = CENTER)
espaciopass.pack()
botones = Frame(master)
botones.config(pady = 10)
botones.pack()
generar = Button(botones, text = "Generar contraseña", command = generar_pass)
generar.grid( row = 0, column = 0)
reiniciar = Button(botones, text = "Reiniciar", command = reinicio)
reiniciar.grid(row = 0, column =1)
root.mainloop()

