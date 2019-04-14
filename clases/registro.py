

class Registro:

    def __init__(self, posicion, clase):
        self.posicion = posicion
        self.clase = clase

    def __str__(self):
        return self.posicion.__str__() + ' ' + self.clase