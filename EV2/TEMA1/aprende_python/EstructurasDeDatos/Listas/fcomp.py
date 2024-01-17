# *********************************
# APLICANDO FUNCIÓN POR COMPRENSIÓN
# *********************************


def run(xmin: int, xmax: int) -> list:
    values = []
    for x in range(xmin, xmax + 1):
        values += [x * 3 + 2]

    return values


if __name__ == '__main__':
    run(0, 10)
