# *************************
# LA MULTIPLICACIÓN DE JACK
# *************************


def run(n: int) -> int:
    return n * 5 ** (len(str(abs(n))))


if __name__ == '__main__':
    run(3)
