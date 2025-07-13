class ColaDinamica:
    
    def __init__(self):
        self.pila = []

    def esta_vacia(self):
        return len(self.pila) == 0

    def encolar(self, elemento):
        self.pila.append(elemento)
        print(f"Encolado: {elemento}")

    def desapilar(self):
        if self.esta_vacia():
            print("Error: La pila está vacía. No se puede desapilar.")
            return None
        elemento = self.pila[0]
        print(f"Desapilado: {elemento}")
        return elemento

    def cima(self):
        if self.esta_vacia():
            print("Error: La pila está vacía. No hay cima.")
            return None
        return self.pila[-1] # El último elemento de la lista

    def dimension(self):
        return len(self.pila)
