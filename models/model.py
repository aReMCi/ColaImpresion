from .PilaDinamica import PilaDinamica

class DataModel:
    def __init__(self):
        self.lista = PilaDinamica()

    def add_data(self, item):
        self.lista.apilar(item)

    def del_data(self):
        return self.lista.desapilar()
    
    def get_primero(self):
        return self.lista.cima()
    
    def get_cantidad(self):
        return self.lista.dimension()