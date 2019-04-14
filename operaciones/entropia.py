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





