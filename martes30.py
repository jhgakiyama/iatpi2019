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


midataset = Dataset("datasetchico.csv")

# midataset.imprimir()

# midataset.ordenar_x()
# midataset.imprimir()
# midataset.ordenar_y()
# midataset.imprimir()

# lista = [11,22,33,4,5,4,4,3,5,5]
# sinrepetir = set(lista)
# print(sinrepetir)
# lista = sorted(list(sinrepetir))
# print(lista)


def calcular_entropia(dataset):
    class1, class2 = 0, 0

    for valor in dataset:
        if valor[2]:
            class1 += 1
        else:
            class2 += 1
    
    total = len(dataset)
    
    prob1 = class1 / total
    prob2 = class2 / total

    try:
        entropia = -(prob1 * log2(prob1) + prob2 * log2(prob2))
    except ValueError:
        return 0

    return round(entropia, 3)


def funciondoctorK(dataset):
    class1, class2 = 0, 0
    
    for valor in dataset:
        if valor[2]:
            class1 += 1
        else:
            class2 += 1

    if class1 == len(dataset) or class2 == len(dataset):
        print('CASO BASE 1 . hacer NODO :3 ')
        return 
    
    elif len(dataset) == 0:
        print('CASO BASE 2 . hacer HOJA c; ')
        return 

    else:
        # ordenamos los valores del atributo X de formar ascendente
        dataset.sort(key=lambda x: x[0])
        
        entropia_total = calcular_entropia(dataset)

        maxganx = 0
        for i in range(len(dataset)-1):
            cjto1 = dataset[0:i+1]
            cjto2 = dataset[i+1:len(dataset)]

            entropia_cjto1 = calcular_entropia(cjto1)
            entropia_cjto2 = calcular_entropia(cjto2)

            ganancia_1 = entropia_total - entropia_cjto1
            ganancia_2 = entropia_total - entropia_cjto2

            if ganancia_1 > maxganx:
                maxganx = ganancia_1
                umbralx = i
            elif ganancia_2 > maxganx:
                maxganx = ganancia_2
                umbralx = i

            print(maxganx)
            print(umbralx)
            print()



funciondoctorK(midataset.dataset)
