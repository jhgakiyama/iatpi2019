from operaciones import logaritmo_base_2

def entropy_dataset(dataset):
    size = len(dataset.registros)
    c1 = 0
    c2 = 0

    clase1 = dataset.registros[0].clase

    for i in dataset.registros:
        if i.clase == clase1:
            c1 += 1
        else:
            c2 += 1

    prob1 = c1 / size
    prob2 = c2 / size

    # contolar log(0)

    return (prob1 * log2(prob1) + prob2 * log2(prob2)) * (-1)