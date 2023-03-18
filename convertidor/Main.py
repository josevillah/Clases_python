# System imports
from tkinter import *
from pathlib import Path
from PIL import ImageTk, Image
import os

# My imports
from Windows import *

# This function is used for the windows tk configurations
def config(root):
    background = '#3d474b'
    root.config(bg=background)
    root.title("Convertidor de Imagenes")
    root.geometry("410x410+550+200")
    root.resizable(0, 0)

    # logo Configurations
    ruta = __file__.replace('Main.py', '')
    images = ruta+'\\imageSystem'
    path = Path(os.path.join(os.getcwd(), images))
    img = os.path.join(path, 'icon.png')
    icono = PhotoImage(file=img)
    root.iconphoto(True, icono)

# This function is used for start the system
def main():
    root = Tk()
    config(root)
    app = Main(root)
    app.mainloop()

# Execution
if __name__ == '__main__':
    main()


