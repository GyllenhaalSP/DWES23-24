# ******************
# TUPLAS Y CONJUNTOS
# ******************


def run(input: tuple) -> tuple:
    primer_conjunto = set()
    segundo_conjunto = set()

    for dupla in input:
        primer_conjunto.add(dupla[0])
        segundo_conjunto.add(dupla[1])

    return primer_conjunto, segundo_conjunto


if __name__ == '__main__':
    run(((4, 3), (8, 2), (7, 5), (8, 2), (9, 1)))
