from math import log2

condicion = ["R", "R", "R", "L", "R", "L"]

def entropia_atributo(dataset, atributo):
    conjunto = set()

    primera = dataset.puntos[0]

    diccionario = {}

    if atributo == 'x':
        diccionario[primera.x] = 0
    else:
        diccionario[primera.y] = 0

    print(diccionario)

    for i in dataset.puntos:
        if atributo == 'x':
            diccionario[primera.x] += 1
        else:
            diccionario[primera.y] += 1

    size = len(dataset.puntos)








class dataset():
    puntos = []

    def agregar_punto(self, punto):
        self.puntos.append(punto)

    def listar(self):
        for i in self.puntos:
            print(i)

    def entropy_class(self):
        size = len(self.puntos)
        c1 = 0
        c2 = 0

        clase1 = self.puntos[0].clase

        for i in self.puntos:
            if i.clase == clase1:
                c1 += 1
            else:
                c2 += 1

        prob1 = c1/size
        prob2 = c2/size

        # contolar log(0)

        return (prob1*log2(prob1) + prob2*log2(prob2)) * (-1)





punto1 = punto('tecnica', 'si', 'regular')
punto2 = punto('tecnica', 'si', 'regular')
punto3 = punto('no tecnica', 'si', 'regular')
punto4 = punto('no tecnica', 'no', 'libre')
punto5 = punto('tecnica', 'si', 'regular')
punto6 = punto('tecnica', 'no', 'libre')

midataset = dataset()

midataset.agregar_punto(punto1)
midataset.agregar_punto(punto2)
midataset.agregar_punto(punto3)
midataset.agregar_punto(punto4)
midataset.agregar_punto(punto5)
midataset.agregar_punto(punto6)

midataset.listar()

print(midataset.entropy_class())

print(entropia_atributo(midataset, 'x'))
# print(entropia_atributo(midataset, 'y'))