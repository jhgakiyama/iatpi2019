from math import log2


class Dataset:
    """Clase Base para un Dataset
    :param filename
    """

    def __init__(self, filename):
        self.filename = filename
        self.class1 = 0
        self.class2 = 0
        self.dataset = self.cargar_dataset(filename)
        self.total = len(self.dataset)
        self.__original = self.cargar_dataset(filename)
        self.entropia = self.__entropy_class()

    def __str__(self):
        return "Dataset. File: {2} | Entropia(D): {0} | Tamaño: {1}".format(self.entropia, self.total, self.filename)

    def cargar_dataset(self, filename):
        """ Leo el archivo.txt y lo cargo a una lista """

        with open(filename) as mi_archivo:

            dataset = []

            for line in mi_archivo:

                dato = line.split(',')
                datonuevo = []

                for i in dato:
                    datonuevo.append(float(i))

                dataset.append(datonuevo)

        return dataset

    def imprimir(self):

        for i in self.dataset:
            print(i)

    def __entropy_class(self):

        # class1 son los cuadrados
        # class2 son los circulos

        for valor in self.dataset:
            if valor[2]:
                self.class1 += 1
            else:
                self.class2 += 1

        prob1 = self.class1 / self.total
        prob2 = self.class2 / self.total

        entropia = -(prob1 * log2(prob1) + prob2 * log2(prob2))

        return round(entropia, 3)

    def ordenar_x(self):
        self.dataset.sort(key=lambda x: x[0])

    def ordenar_y(self):
        self.dataset.sort(key=lambda x: x[1])

    def original(self):
        return self.__original

    def nuevo_dataset(self, lista):
        pass


midataset = Dataset("dataset.csv")

print(midataset.entropia)

midataset.imprimir()

# midataset.ordenar_x()
# midataset.imprimir()
# midataset.ordenar_y()
# midataset.imprimir()
