# ********************************
# OBTENIENDO EL NÚMERO DE PALABRAS
# ********************************


def run(text: str) -> int:
    return len(text.split())


if __name__ == '__main__':
    run('Before software can be reusable it first has to be usable')
