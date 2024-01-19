# **********************
# MEZCLANDO DICCIONARIOS
# **********************


def run(d1: dict, d2: dict) -> dict:
    merged = {}

    for clave in d1:
        merged[clave] = d1[clave]

    for clave in d2:
        merged[clave] = d2[clave]

    return merged


if __name__ == '__main__':
    run({'a': 1, 'b': 2}, {'a': 3, 'c': 4})