from operaciones.logaritmo_base_2 import logaritmo_base_2
from clases.dataset import Dataset
from clases.registro import Registro


def entropy_dataset(dataset: Dataset):
    primer_registro: Registro = dataset.primer_registro()
    registros = dataset.registros
    primer_clase = primer_registro.clase

    size = len(registros)
    c1 = 0
    c2 = 0

    # cuento la cantidad de elementos de cada "clase" hay en el dataset
    for registro in registros:
        if registro.clase == primer_clase:
            c1 += 1
        else:
            c2 += 1

    n1 = c1 / size
    n2 = c2 / size

    return (n1 * logaritmo_base_2(n1) + n2 * logaritmo_base_2(n2)) * (-1)
