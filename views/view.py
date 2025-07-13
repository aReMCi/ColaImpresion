from tkinter import Tk, Frame, Label, Button, Entry, ttk, filedialog

class View:
    def __init__(self, master):
        self.master = master
        master.title("Cola de Impresión")
        master.geometry("400x500")


        self.frame = Frame(master)
        self.frame.pack()

        #Lista de elementos
        self.tree = ttk.Treeview(self.frame, columns=("Nro", "Elemento"), show='headings')
        self.tree.heading("Nro", text="Nro")
        self.tree.column("Nro", width=50)
        self.tree.heading("Elemento", text="Documento")
        self.tree.column("Elemento", width=200)
        self.tree.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        #Label de estado
        self.status_label = Label(self.frame, text="Listo")
        self.status_label.grid(row=2, column=0, columnspan=2, pady=5)

        #Frame Para Botones
        self.botones_frame = Frame(self.frame)
        self.botones_frame.grid(row=1, column=0, columnspan=2, pady=10)

        #Inicializacion de Botones
        self.on_add_button = None  

        #Boton Agregar
        self.add_button = Button(self.botones_frame, text="Agregar", command=self._handle_add_button_click)
        self.add_button.grid(row=0, column=0, padx=5)

    def ask_open_file(self):
        return filedialog.askopenfilenames(
            title="Abrir Archivo",
            filetypes=[("Todos los Archivos", "*.*")]
        )
    
    def _handle_add_button_click(self):
        if self.on_add_button:
            self.on_add_button()
    
    def show_status(self, text):
        self.status_label.config(text=text)