import tkinter as tk
from models.model import DataModel as Model
from controllers.controller import Controller
from views.view import View

ventana = tk.Tk()

#Creacion del MVC
model = Model()
view = View(ventana)
controller = Controller(model,view)

if __name__ == "__main__":  
    ventana.mainloop()
