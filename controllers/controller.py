from models.model import DataModel as Model
from views.view import View

class Controller:
    def __init__(self, model,view):
        self.model = model
        self.view = view

        self.view.on_add_button = self.add_item
        self.view.on_delete_button = self.delete_item
        self.imprimiendo = False

    def iniciar_impresion(self):
        if not self.imprimiendo and self.model.get_cantidad() > 0:
            self.imprimiendo = True
            self._imprimir_siguiente()

    def _imprimir_siguiente(self):
        if self.model.get_cantidad() == 0:
            self.imprimiendo = False
            return
        #simulando 5 segundos de impresión
        self.view.show_status("Imprimiendo...")
        self.view.master.after(10000, self._finalizar_impresion)

    def _finalizar_impresion(self):
        removed_item = self.model.del_data()
        if removed_item:
            #Eliminar el primer elemento
            for item in self.view.tree.get_children():
                if self.view.tree.item(item, 'values')[1] == removed_item:
                    self.view.tree.delete(item)
                    break
        self.view.show_status("Listo")

        if self.model.get_cantidad() > 0:
            self._imprimir_siguiente()
        else:
            self.imprimiendo = False
            self.view.show_status("No hay más documentos para imprimir.")

    def add_item(self):
        file_paths = self.view.ask_open_file()  
        if file_paths:
            # Procesar archivo
            for file_path in file_paths:
                self.model.add_data(file_path)
                self.view.tree.insert("", "end", values=(self.model.get_cantidad(), file_path))
            self.iniciar_impresion()

    def delete_item(self):
        if not self.model.get_cantidad():
            print("No hay elementos para eliminar.")
            return

        removed_item = self.model.del_data()
        if removed_item:
            print(f"Elemento eliminado: {removed_item}")
            # Actualizar la vista
            for item in self.view.tree.get_children():
                if self.view.tree.item(item, 'values')[1] == removed_item:
                    self.view.tree.delete(item)
                    break
        else:
            print("No se pudo eliminar el elemento.")  