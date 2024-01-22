# **************************
# BARICENTRO DE UN TRIÁNGULO
# **************************


def run(A: list, B: list, C: list) -> tuple:
    x, y = [sum(coordenadas) / len((A, B, C)) for coordenadas in zip(A, B, C)]
    return round(x, 4), round(y, 4)


if __name__ == '__main__':
    run([4, 6], [12, 4], [10, 10])