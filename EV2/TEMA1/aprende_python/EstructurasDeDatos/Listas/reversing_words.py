# *************************
# PALABRAS EN ORDEN INVERSO
# *************************


def run(text: str) -> str:
    return " ".join(text.split(" ")[::-1]).lower()


if __name__ == '__main__':
    run('Hello World')