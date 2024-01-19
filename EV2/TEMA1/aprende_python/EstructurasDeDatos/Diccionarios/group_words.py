# ******************
# AGRUPANDO PALABRAS
# ******************


def run(words: list) -> dict:
    return {key: [word for word in words if word.startswith(key)] for key in set([word[0] for word in words])}


if __name__ == '__main__':
    run(['mesa', 'móvil', 'barco', 'coche', 'avión', 'bandeja', 'casa', 'monitor', 'carretera', 'arco'])
