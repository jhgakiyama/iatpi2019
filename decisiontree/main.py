from clases.dataset import Dataset
from clases.registro import Registro
from clases.posicion import Posicion

p1 = Posicion('tecnica', 'si')
p2 = Posicion('tecnica', 'no')
p3 = Posicion('no tecnica', 'si')
p4 = Posicion('no tecnica', 'no')

r1 = Registro(p1, 'regular')
r2 = Registro(p1, 'regular')
r3 = Registro(p3, 'regular')
r4 = Registro(p4, 'libre')
r5 = r1
r6 = Registro(p2, 'libre')

mydataset = Dataset()
mydataset.agregar_registro(r1)
mydataset.agregar_registro(r2)
mydataset.agregar_registro(r3)
mydataset.agregar_registro(r4)
mydataset.agregar_registro(r5)
mydataset.agregar_registro(r6)

print(mydataset.mostrar())
