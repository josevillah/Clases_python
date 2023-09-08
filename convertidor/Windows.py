from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
# My imports
from Controller import *

class Main(Frame):
    # Constructor of class
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.style = ttk.Style()
        self.background = '#3d474b'
        self.text = '#fff'
        self.file = ''
        self.controller = Controller()
        self.grid()
        self.createWidgets()
        self.config(bg=self.background)

    def openFile(self):
        self.file = filedialog.askopenfilename(title='Selecciona tu imagen')
        if self.file != '':
            name = Path(self.file).name
            self.fileName.config(state='normal')
            self.fileName.delete(0, END)
            self.fileName.insert(0, name)
            self.fileName.config(state='disable')
    
    def openDir(self):
        self.file = filedialog.askdirectory(title='Selecciona tu Carpeta')
        if self.file != '':
            name = Path(self.file).name
            self.fileName.config(state='normal')
            self.fileName.delete(0, END)
            self.fileName.insert(0, name)
            self.fileName.config(state='disable')
    
    def toPng(self):
        if self.file != '':
            if self.controller.sendFile(self.file, 'png'):
                messagebox.showinfo(message="La conversion se realizo correctamente", title="Información")
            else:
                messagebox.showerror(message="Algo ha ocurrido!", title="Error")
    
    def toJpg(self):
        if self.file != '':
            if self.controller.sendFile(self.file, 'jpeg'):
                messagebox.showinfo(message="La conversion se realizo correctamente", title="Información")
            else:
                messagebox.showerror(message="Algo ha ocurrido!", title="Error")

    def toWebp(self):
        if self.file != '':
            if self.controller.sendFile(self.file, 'webp'):
                messagebox.showinfo(message="La conversion se realizo correctamente", title="Información")
            else:
                messagebox.showerror(message="Algo ha ocurrido!", title="Error")
   
    def toIco(self):
        if self.file != '':
            if self.controller.sendFile(self.file, 'ico'):
                messagebox.showinfo(message="La conversion se realizo correctamente", title="Información")
            else:
                messagebox.showerror(message="Algo ha ocurrido!", title="Error")

    def deleteImages(self):
        if messagebox.askokcancel(message="¿Desea Eliminar todos los archivos dentro del directorio 'Terminado'?", title="Título"):
            if self.controller.deleteImages():
                messagebox.showinfo(message="La operación se realizo correctamente", title="Información")
            else:
                messagebox.showerror(message="Error: Verifique que la carpeta no esté vacía", title="Error")
        else:
            print('cancelando')


    # This function is used for create the widgets in de window
    def createWidgets(self):

        # Constructors widgets
        title = Label(self, text = 'Conversor', background=self.background, fg=self.text, font=('Helvetica', 20, 'bold'))
        self.fileName = Entry(self, background=self.text, fg=self.background, font=('Helvetica', 10, 'bold'))
        self.fileName.insert(0, 'Ningun Archivo Seleccionado')
        self.fileName.config(state='disabled')
        selectFileButton = Button(self, text='Seleccionar Imagen', command= self.openFile, relief=FLAT, background='#1cb3d4', fg=self.text, font=('Helvetica', 10, 'bold'))
        selectDirButton = Button(self, text='Seleccionar Carpeta', command= self.openDir, relief=FLAT, background='#1F30C9', fg=self.text, font=('Helvetica', 10, 'bold'))
        nameOptions = Label(self, text = 'Opciones', background=self.background, fg=self.text, font=('Helvetica', 16, 'normal'))
        pngButton = Button(self, text='PNG', relief=FLAT, command=self.toPng, background='#28c740', fg=self.text, font=('Helvetica', 10, 'bold'))
        jpgButton = Button(self, text='JPG', relief=FLAT, command=self.toJpg, background='#2850c7', fg=self.text, font=('Helvetica', 10, 'bold'))
        webpButton = Button(self, text='WEBP', relief=FLAT, command=self.toWebp, background='#c78f28', fg=self.text, font=('Helvetica', 10, 'bold'))
        tifButton = Button(self, text='ICO', relief=FLAT, command=self.toIco, background='#5F13E4', fg=self.text, font=('Helvetica', 10, 'bold'))
        delete = Button(self, text='Borrar', relief=FLAT, command=self.deleteImages, background='#cf1d1d', fg=self.text, font=('Helvetica', 10, 'bold'))

        # show widgets
        title.grid(row=0, column=0, columnspan=4, ipady=20, ipadx=135, sticky="NESW")
        self.fileName.grid(row=1, column=0, columnspan=4, ipady=5, pady=10, padx=10, sticky="NESW")
        selectFileButton.grid(row=2, column=1, columnspan=2, ipady=5, pady=10, sticky="NESW")
        selectDirButton.grid(row=3, column=1, columnspan=2, ipady=5, pady=10, sticky="NESW")
        nameOptions.grid(row=4, column=0, columnspan=4, ipady=10, ipadx=135, sticky="NESW")
        pngButton.grid(row=5, column=0, ipady=5, ipadx=5, pady=10)
        jpgButton.grid(row=5, column=1, ipady=5, ipadx=5, pady=10)
        webpButton.grid(row=5, column=2, ipady=5, ipadx=5, pady=10)
        tifButton.grid(row=5, column=3, ipady=5, ipadx=5, pady=10)
        delete.grid(row=6, column=3, ipady=5, ipadx=5, pady=10)
