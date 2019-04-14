

class Posicion:
    x: str
    y: str

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return self.x + ' ' + self.y
