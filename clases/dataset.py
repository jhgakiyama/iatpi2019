

class Dataset:

    def __init__(self, registros = []):
        self.registros = registros

    def agregar_registro(self, registro):
        self.registros.append(registro)

    def mostrar(self):
        for i in self.registros:
            print(i)