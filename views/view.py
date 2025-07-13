from tkinter import Tk, Frame, Label, Button, Entry

class View:
    def __init__(self, master):
        self.master = master
        master.title("Cola de Impresión")
        master.geometry("400x300")


        self.frame = Frame(master)
        self.frame.pack()
       