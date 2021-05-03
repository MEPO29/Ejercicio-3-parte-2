# PROGRAMA CREADO POR
# MARIO PUENTE
# CARNE 21290

# importar modulo tkinter para hacer un GUI
from tkinter import *
from tkinter import ttk 
from functools import partial

# definir la impresion del recibo
def recibo():
	tott = round(float(totText.get()), 2)
	top = Toplevel()
	top.geometry("400x400")
	top.config(bg="light blue")

	label = Label(top, text='=============RECIBO=============')
	label.pack()
	label.config(bg="light blue")
	heading = Label(top, text='Producto 		Precio 			Cantidad')
	heading.pack()
	heading.config(bg="light blue")

	for rama in listBox.get_children():
		producto = (listBox.item(rama, 'values')[0])
		precio = float(listBox.item(rama, 'values')[1])
		cantidad = float(listBox.item(rama, 'values')[2])
		total = float(listBox.item(rama, 'values')[3])
		producto1 = Label(top, text=f'{producto}		{precio}		{cantidad}')
		producto1.config(bg="light blue")
		producto1.pack()

	total = Label(top, text=f'Total\t{tott}')
	total.pack()
	total.config(bg="light blue")

def comandoClear():
	for i in listaEntries:
		i.delete(0, END)
		i.insert(0, "")
	for i in listaChkValues:
		i.set(0)
	totText.set('')
	listBox.delete(*listBox.get_children())

# definir el GUI donde el cajero escoge cuales productos lleva y cuantos de cada uno
def show():
	total = 0
	if (var1.get()):
		precio = 1.19
		cantidad = float(e1.get())
		listaInventario[0] -= int(cantidad)
		inv1.set(listaInventario[0])
		total = (precio * cantidad)
		tempList = [['Leche', precio, e1.get(), total]]
		tempList.sort(key = lambda e: e[1], reverse = True)
		if listaInventario[0] <= 0:
			inv1.set(tempList[0][0]+' AGOTADO')
		for i, (producto, precio, cantidad, total) in enumerate(tempList, start = 1):
			if listaInventario[0] < 0:
				break
			else:
				listBox.insert("", "end", values = (producto, precio, cantidad, total))

	if (var2.get()):
		precio = 1.45
		cantidad = float(e2.get())
		listaInventario[1] -= int(cantidad)
		inv2.set(listaInventario[1])
		total = (precio * cantidad)
		tempList = [['Galletas', precio, e2.get(), total]]
		tempList.sort(key = lambda e: e[1], reverse = True)
		if listaInventario[1] <= 0:
			inv2.set(tempList[0][0]+' AGOTADO')
		for i, (producto, precio, cantidad, total) in enumerate(tempList, start = 1):
			if listaInventario[1] < 0:
				break
			else:
				listBox.insert("", "end", values = (producto, precio, cantidad, total))

	if (var3.get()):
		precio = 1.90
		cantidad = float(e3.get())
		listaInventario[2] - int(cantidad)
		inv3.set(listaInventario[2])
		total = (precio * cantidad)
		tempList = [['Mantequilla', precio, e3.get(), total]]
		tempList.sort(key = lambda e: e[1], reverse = True)
		if listaInventario[2] <= 0:
			inv3.set(tempList[0][0]+' AGOTADO')
		for i, (producto, precio, cantidad, total) in enumerate(tempList, start = 1):
			if listaInventario[2] < 0:
				break
			else:
				listBox.insert("", "end", values = (producto, precio, cantidad, total))

	if (var4.get()):
		precio = 2.59
		cantidad = float(e4.get())
		listaInventario[3] - int(cantidad)
		inv4.set(listaInventario[3])
		total = (precio * cantidad)
		tempList = [['Queso', precio, e4.get(), total]]
		tempList.sort(key = lambda e: e[1], reverse = True)
		if listaInventario[3] <= 0:
			inv4.set(tempList[0][0]+' AGOTADO')
		for i, (producto, precio, cantidad, total) in enumerate(tempList, start = 1):
			if listaInventario[3] < 0:
				break
			else:
				listBox.insert("", "end", values = (producto, precio, cantidad, total))

	if (var5.get()):
		precio = 4.99
		cantidad = float(e5.get())
		listaInventario[4] - int(cantidad)
		inv5.set(listaInventario[4])
		total = (precio * cantidad)
		tempList = [['Pan', precio, e5.get(), total]]
		tempList.sort(key = lambda e: e[1], reverse = True)
		if listaInventario[4] <= 0:
			inv5.set(tempList[0][0]+' AGOTADO')
		for i, (producto, precio, cantidad, total) in enumerate(tempList, start = 1):
			if listaInventario[4] < 0:
				break
			else:
				listBox.insert("", "end", values = (producto, precio, cantidad, total))

	if (var6.get()):
		precio = 3.65
		cantidad = float(e6.get())
		listaInventario[5] - int(cantidad)
		inv6.set(listaInventario[5])
		total = (precio * cantidad)
		tempList = [['Jalea', precio, e6.get(), total]]
		tempList.sort(key = lambda e: e[1], reverse = True)
		if listaInventario[5] <= 0:
			inv6.set(tempList[0][0]+' AGOTADO')
		for i, (producto, precio, cantidad, total) in enumerate(tempList, start = 1):
			if listaInventario[5] < 0:
				break
			else:
				listBox.insert("", "end", values = (producto, precio, cantidad, total))

	if (var7.get()):
		precio = 3.15
		cantidad = float(e7.get())
		listaInventario[6] - int(cantidad)
		inv7.set(listaInventario[6])
		total = (precio * cantidad)
		tempList = [['Yogurt', precio, e7.get(), total]]
		tempList.sort(key = lambda e: e[1], reverse = True)
		if listaInventario[6] <= 0:
			inv7.set(tempList[0][0]+' AGOTADO')
		for i, (producto, precio, cantidad, total) in enumerate(tempList, start = 1):
			if listaInventario[6] < 0:
				break
			else:
				listBox.insert("", "end", values = (producto, precio, cantidad, total))

	if (var8.get()):
		precio = 2.15
		cantidad = float(e8.get())
		listaInventario[7] - int(cantidad)
		inv8.set(listaInventario[7])
		total = (precio * cantidad)
		tempList = [['Manzanas', precio, e8.get(), total]]
		tempList.sort(key = lambda e: e[1], reverse = True)
		if listaInventario[7] <= 0:
			inv8.set(tempList[0][0]+' AGOTADO')
		for i, (producto, precio, cantidad, total) in enumerate(tempList, start = 1):
			if listaInventario[7] < 0:
				break
			else:
				listBox.insert("", "end", values = (producto, precio, cantidad, total))

	if (var9.get()):
		precio = 0.99
		cantidad = float(e9.get())
		listaInventario[8] -= int(cantidad)
		inv9.set(listaInventario[8])
		total = (precio * cantidad)
		tempList = [['Naranjas', precio, e9.get(), total]]
		tempList.sort(key = lambda e: e[1], reverse = True)
		if listaInventario[8] <= 0:
			inv9.set(tempList[0][0]+' AGOTADO')
		for i, (producto, precio, cantidad, total) in enumerate(tempList, start = 1):
			if listaInventario[8] < 0:
				break
			else:
				listBox.insert("", "end", values = (producto, precio, cantidad, total))
	if (var10.get()):
		precio = 1.29
		cantidad = float(e10.get())
		listaInventario[9] -= int(cantidad)
		inv10.set(listaInventario[9])
		total = (precio * cantidad)
		tempList = [['Bananos', precio, e10.get(), total]]
		tempList.sort(key = lambda e: e[1], reverse = True)
		if listaInventario[9] <= 0:
			inv10.set(tempList[0][0]+' AGOTADO')
		for i, (producto, precio, cantidad, total) in enumerate(tempList, start = 1):
			if listaInventario[9] < 0:
				break
			else:
				listBox.insert("", "end", values = (producto, precio, cantidad, total))

	sum1 = 0.0
	for rama in listBox.get_children():
		sum1 += float(listBox.item(rama, 'values')[3])
	totText.set(sum1)

# defnir el titulo del GUI, el tamano del canvas y el color de fondo del canvas
root = Tk()
root.title("Sistema de recibos")
root.geometry("830x840")
root['bg'] = 'gray'

# crear la variable totText para llamarla luego, en esta variable se guarda el total de
# la transaccion
totText = StringVar()

# en este label escribo lo que sale hasta arriba (titulo), le cambio el color de fondo 
# y el tipo de letra
Label(root, text = "Sistema de recibos", font = "courier 22 bold", bg = "light blue").place(x=5, y=10)
# label estetico para identificar las casillas de cantidad
Label(root, text = "Cantidad").place(x=140, y=70)

# comienzo a crear los checkboxes de los diferentes productos
var1 = IntVar()
Checkbutton(root, text="Leche", variable=var1).place(x=10, y=90)
 
var2 = IntVar()
Checkbutton(root, text="Galletas", variable=var2).place(x=10, y=120)
 
var3 = IntVar()
Checkbutton(root, text="Mantequilla", variable=var3).place(x=10, y=150)
 
var4 = IntVar()
Checkbutton(root, text="Queso", variable=var4).place(x=10, y=180)
 
var5 = IntVar()
Checkbutton(root, text="Pan", variable=var5).place(x=10, y=210)

var6 = IntVar()
Checkbutton(root, text="Jalea", variable=var6).place(x=10, y=240)
 
var7 = IntVar()
Checkbutton(root, text="Yogurt", variable=var7).place(x=10, y=270)
 
var8 = IntVar()
Checkbutton(root, text="Manzanas", variable=var8).place(x=10, y=300)
 
var9 = IntVar()
Checkbutton(root, text="Naranjas", variable=var9).place(x=10, y=330)
 
var10 = IntVar()
Checkbutton(root, text="Bananos", variable=var10).place(x=10, y=360)

# creo las casillas donde se ingresan las cantidades de productos que lleva el cliente
e1 = Entry(root)
e1.place(x=140, y=90)

e2 = Entry(root)
e2.place(x=140, y=120)

e3 = Entry(root)
e3.place(x=140, y=150)

e4 = Entry(root)
e4.place(x=140, y=180)

e5 = Entry(root)
e5.place(x=140, y=210)

e6 = Entry(root)
e6.place(x=140, y=240)

e7 = Entry(root)
e7.place(x=140, y=270)

e8 = Entry(root)
e8.place(x=140, y=300)

e9 = Entry(root)
e9.place(x=140, y=330)

e10 = Entry(root)
e10.place(x=140, y=360)

listaEntries = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10]
listaInventario = [20,32,15,15,20,18,35,35,40,23]
listaChkValues = [var1, var2, var3, var4, var5, var6, var7, var8, var9, var10]

inv1 = IntVar(root, listaInventario[0])
Label(root, textvariable = inv1, bg = 'gray').place(x=300, y=90)

inv2 = IntVar(root, listaInventario[1])
Label(root, textvariable = inv2, bg = 'gray').place(x=300, y=120)

inv3 = IntVar(root, listaInventario[2])
Label(root, textvariable = inv3, bg = 'gray').place(x=300, y=150)

inv4 = IntVar(root, listaInventario[3])
Label(root, textvariable = inv4, bg = 'gray').place(x=300, y=180)

inv5 = IntVar(root, listaInventario[4])
Label(root, textvariable = inv5, bg = 'gray').place(x=300, y=210)

inv6 = IntVar(root, listaInventario[5])
Label(root, textvariable = inv6, bg = 'gray').place(x=300, y=240)

inv7 = IntVar(root, listaInventario[6])
Label(root, textvariable = inv7, bg = 'gray').place(x=300, y=270)

inv8 = IntVar(root, listaInventario[7])
Label(root, textvariable = inv8, bg = 'gray').place(x=300, y=300)

inv9 = IntVar(root, listaInventario[8])
Label(root, textvariable = inv9, bg = 'gray').place(x=300, y=330)

inv10 = IntVar(root, listaInventario[9])
Label(root, textvariable = inv10, bg = 'gray').place(x=300, y=360)

# defino el label del total de la venta para desplegarlo en el GUI inicial
total = Label(root, bg = 'gray', font = "courier 22 bold", textvariable = round(float(totText.get()), 2)).place(x=650, y=10)

# creo el boton para agregar los productos a la cuenta
Button(root, text="Agregar a la cuenta", command=show, height=3, width=40).place(x=10, y=500)
# creo el boton para imprimir el recibo, este sale en una ventana nueva

reset = Button(root, text = ' Nueva transaccion ',
	command = comandoClear, height = 3, width = 13).place(x=700, y=180 )
Button(root, text = "Imprimir", command = recibo, height = 3, width = 13).place(x=700, y=120)
# defino las columnas que se desplegan en el estado de cuenta
cols = ('Producto', 'Precio', 'Cantidad', 'Total')
listBox = ttk.Treeview(root, columns = cols, show = 'headings')

for col in cols:
	listBox.heading(col, text = col)
	listBox.grid(row = 1, column = 0, columnspan = 2)
	listBox.place(x=10, y=600)

root.mainloop()