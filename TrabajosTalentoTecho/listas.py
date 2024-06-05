class Listas:
    def __init__(self):
        self.lista = []

    def index(self, elemento):
        return self.lista.index(elemento)

    def append(self, elemento):
        self.lista.append(elemento)

    def extend(self, elementos):
        self.lista.extend(elementos)

    def insert(self, indice, elemento):
        self.lista.insert(indice, elemento)

    def remove(self, elemento):
        self.lista.remove(elemento)

    def pop(self, indice=None):
        return self.lista.pop(indice)

    def reverse(self):
        self.lista.reverse()

    def sort(self):
        self.lista.sort()

    def count(self, elemento):
        return self.lista.count(elemento)
