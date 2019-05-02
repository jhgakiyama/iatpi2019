from math import log2

MIARCHIVO = "dataset.csv"
# MIARCHIVO = "solocero.csv"
# MIARCHIVO = "solouno.csv"


def cargar_dataset(filename):
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


DATASET_ORIGINAL = cargar_dataset(MIARCHIVO)


def contar_clases(dataset):
    class1, class2 = 0, 0

    for valor in dataset:
        if valor[2]:
            class1 += 1
        else:
            class2 += 1

    return class1, class2


def calcular_entropia(dataset):
    class1, class2 = contar_clases(dataset)

    try:
        total = len(dataset)

        prob1 = class1 / total
        prob2 = class2 / total

        entropia = -(prob1 * log2(prob1) + prob2 * log2(prob2))

    except (ValueError, ZeroDivisionError):  # cuando la prob es cero
        return 0

    return round(entropia, 3)


def mejorentropia(dataset_original, col):
    entropia_total = dataset_original.entropia #todo cual es la longitud del dataset ? n total (con valores repetidos )o n con los valores que NO se repiten
    lista = []
    # dataset = dataset_original.dataset[:]
    dataset = dataset_original.dataset.copy()
    dataset.sort(key=lambda x: x[col])
    # todo ordenar y despues eliminar los repetidos ? aca recien tengo que calcular la entropia ?

    print(dataset_original.dataset)
    print(dataset)

    maxgan, umbral = 0, 0

    for i in range(len(dataset) - 1):
        cjto1 = dataset[0:i + 1]
        cjto2 = dataset[i + 1:len(dataset)]

        entropia_cjto1 = calcular_entropia(cjto1)
        entropia_cjto2 = calcular_entropia(cjto2)

        ganancia_1 = entropia_total - entropia_cjto1
        ganancia_2 = entropia_total - entropia_cjto2

        if ganancia_1 > maxgan:
            maxgan = ganancia_1
            umbral = i
        elif ganancia_2 > maxgan:
            maxgan = ganancia_2
            umbral = i

    return maxgan, umbral


def recursiva(dataset):

    if (dataset.class1 == dataset.total or dataset.class2 == dataset.total) and dataset.total != 0:
        print('CASO BASE 1 . hacer NODO  PURO:3 ')
        if dataset.class1 == dataset.total:
            print("NODO HOJA: clase --> 1")
            print(dataset.class1)
        else:
            print("NODO HOJA: clase --> 0")
            print(dataset.class2)
        return

    elif not dataset.dataset:
        print('CASO BASE 2 . hacer HOJA  "impura" ')
        return

    else:
        # ordenamos los valores del atributo X de formar ascendente

        print('calculo de entropia para X')
        mex, umbralx = mejorentropia(dataset, 0)
        print('calculo de entropia para Y')
        mey, umbraly = mejorentropia(dataset, 1)

        print(mex)
        print(umbralx)
        print()

        print(mey)
        print(umbraly)
        print()


class Dataset:
    """Clase Base para un Dataset
    :param dataset
    """

    def __init__(self, dataset):
        self.dataset = dataset
        self.total = len(self.dataset)
        self.entropia = calcular_entropia(self.dataset)
        self.class1, self.class2 = contar_clases(dataset)

    def __str__(self):
        return "Dataset. Entropia(D): {0} | Tamaño: {1}".format(self.entropia, self.total)

    def imprimir(self):

        for i in self.dataset:
            print(i)


midataset = Dataset(DATASET_ORIGINAL)


recursiva(midataset)
