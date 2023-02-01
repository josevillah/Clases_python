from tkinter import *

# iniciar tk
app = Tk()

# tamaño de la ventana
app.geometry('1020x630+0+0')

# evitar maximizar
app.resizable(0, 0)

# agregar titulo
app.title("Restaurante - Sistema de Facturacion")

# color de fondo
app.config(bg='burlywood')

# Panel superior
"""
tipos de relieves(relief):
FLAT
RAISED
SUNKEN
GROOVE
RIDGE
"""
top = Frame(app, bd=1, relief=FLAT)
top.pack(side=TOP)

# Etiqueta Titulo
titulo = Label(
    top, text="Sistema de Facturacion", fg='azure4',
    font=('Dosis', 50), bg='burlywood', width=26
)

# Posicionamos el título en una grilla que se encontrara en las columnas y filas espesificas
titulo.grid(row=0, column=0)

"""Panel Izquierdo"""

# Panel Izquierdo que contendra sub paneles
panel_izquierdo = Frame(app, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel que estara debajo dentro del panel izquerdo
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

# Panel Comidas
panel_comidas = LabelFrame(
    panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'),
    bd=1, relief=FLAT, fg='azure4'
)

panel_comidas.pack(side=LEFT)

# Panel Bebidas
panel_bebidas = LabelFrame(
    panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'),
    bd=1, relief=FLAT, fg='azure4'
)
panel_bebidas.pack(side=LEFT)

# Panel Postres
panel_postres = LabelFrame(
    panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),
    bd=1, relief=FLAT, fg='azure4'
)
panel_postres.pack(side=LEFT)


"""Panel Derecho"""
# Panel Derecha que contendra sub paneles
panel_derecha = Frame(app, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# Panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack(side=TOP)

# Panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack(side=TOP)

# Panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack(side=TOP)


# Lista de productos
lista_comidas = ['Pollo', 'Cordero', 'Salmon', 'Merluza', 'Kebab', 'Calamar', 'Carne', 'Pizza']
lista_bebidas = ['Agua', 'Soda', 'Coca-Cola', 'Vino', 'Cerveza', 'Ron', 'Sprite', 'Fanta']
lista_postres = ['Helado', 'Fruta', 'Brownie', 'Flan', 'Pastel', 'Torta', 'Cake', 'Tres Leches']

# Generar items Comida
variables_comida = []
# datos para inputs text
cuadros_comida = []
texto_comida = []

contador = 0
for comida in lista_comidas:

    # Crear Checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(
        panel_comidas, text=comida.title(), font=('Dosis', 19, 'bold'),
        onvalue=1, offvalue=0, variable=variables_comida[contador]
    )
    comida.grid(row=contador, column=0, sticky=W)

    # Crear inputs
    cuadros_comida.append('')
    texto_comida.append('')
    cuadros_comida[contador] = Entry(
        panel_comidas, font=('Dosis', 18, 'bold'),
        bd=1, width=6, state=DISABLED, textvariable=texto_comida[contador]
    )
    cuadros_comida[contador].grid(row=contador, column=1)
    contador += 1


# Generar items Bebidas
variables_bebidas = []
# datos para inputs text
cuadros_comida = []
texto_comida = []
contador = 0
for bebida in lista_bebidas:

    # Crear Checkbutton
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    bebida = Checkbutton(
        panel_bebidas, text=bebida.title(), font=('Dosis', 19, 'bold'),
        onvalue=1, offvalue=0, variable=variables_bebidas[contador]
    )
    bebida.grid(row=contador, column=0, sticky=W)

    # Crear inputs
    cuadros_comida.append('')
    texto_comida.append('')
    cuadros_comida[contador] = Entry(
        panel_comidas, font=('Dosis', 18, 'bold'),
        bd=1, width=6, state=DISABLED, textvariable=texto_comida[contador]
    )
    cuadros_comida[contador].grid(row=contador, column=1)
    contador += 1


# Generar items Postres
variables_postres = []
contador = 0
for postre in lista_postres:
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postre = Checkbutton(
        panel_postres, text=postre.title(), font=('Dosis', 19, 'bold'),
        onvalue=1, offvalue=0, variable=variables_postres[contador]
    )
    postre.grid(row=contador, column=0, sticky=W)
    contador += 1

# Evita que la Interfaz se cierre creando un ciclo de la ejecucion
app.mainloop()
