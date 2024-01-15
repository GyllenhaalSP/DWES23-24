# ***************************************
# PRODUCTO CARTESIANO EN CADENAS DE TEXTO
# ***************************************


def run(text1: str, text2: str) -> str:
    return str("".join(["".join((letter1, letter2)) for letter1 in text1 for letter2 in text2]))


if __name__ == '__main__':
    run('xy', '$#')
