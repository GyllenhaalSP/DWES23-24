# ******************************
# VALORES IGUALES EN DICCIONARIO
# ******************************


def run(items: dict) -> bool:

    return len(set(items.values())) == 1 if items else True


if __name__ == '__main__':
    run({'a': 1, 'b': 1, 'c': 1, 'd': 1})