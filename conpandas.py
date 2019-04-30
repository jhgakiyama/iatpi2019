import pandas as pd
import matplotlib.pyplot as plt
from math import log2

# df = pd.read_csv("dataset.csv")
#
# print(df)
#
# print("Tamaño del Dataset")
# print(len(df))
# print()
#
# print("Cantidad de Clase = 0")
#
# print((df.clase == 0).sum())
# print("Cantidad de Clase = 1")
# print((df.clase == 1).sum())
from pandas.core.dtypes.cast import maybe_infer_to_datetimelike


class Dataset:
    """Clase Base para un Dataset
    :param filename
    """

    def __init__(self, filename):
        self.filename = filename
        self.dataset = self.cargar_dataset(filename)
        self.__original = self.cargar_dataset(filename)
        self.total = len(self.dataset)
        self.class1 = (self.dataset.clase == 1).sum()
        self.class0 = (self.dataset.clase == 0).sum()
        self.entropia = self.__entropy_class()

    def __str__(self):
        return "Dataset. File: '{2}' | Entropia(D): {0} | Tamaño: {1}".format(self.entropia, self.total, self.filename)

    def cargar_dataset(self, filename):
        """ Leo el archivo y lo cargo en un DataFrame """

        data_frame = pd.read_csv(filename)

        return data_frame

    def imprimir(self):
        print(self.dataset)

    def __entropy_class(self):

        # class1 son los cuadrados
        # class0 son los circulos

        prob1 = self.class1 / self.total
        prob2 = self.class0 / self.total

        entropia = -(prob1 * log2(prob1) + prob2 * log2(prob2))

        return round(entropia, 3)

    def ordenar_x(self):
        return self.dataset.sort_values(by='x')

    def ordenar_y(self):
        return self.dataset.sort_values(by='y')

    def original(self):
        return self.__original

    def nuevo_dataset(self, lista):
        pass


def dibujar(iris):
    fig = iris[iris.clase == 0].plot(kind='scatter', x='x', y='y', color='blue', label='clase 0')
    iris[iris.clase == 1].plot(kind='scatter', x='x', y='y', color='red', label='clase 1', ax=fig)
    fig.set_xlabel('X - Ancho')
    fig.set_ylabel('Y - Largo')
    fig.set_title('Super grafiquito')
    plt.show()


midataset = Dataset("dataset.csv")

# print(midataset.ordenar_x())

# midataset.dataset.info()
# print(midataset.dataset.describe())
# print(midataset.dataset.groupby('clase').size())

dibujar(midataset.dataset)

for index, row in midataset.dataset.iterrows():
    print(index, row['x'], row['y'], row['clase'])

# tod0 tiene la misma clase1 . caso base 1. tiene q ser una hoja
# dataset = 0 , no hacer tod0 el tratamiento del dataset
#
