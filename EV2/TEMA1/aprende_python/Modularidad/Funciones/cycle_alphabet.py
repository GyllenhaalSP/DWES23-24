# *****************
# ALFABETO CIRCULAR
# *****************
import string


def run(max_letters: int) -> str:
    def generador_alfabeto():
        while True:
            for char in string.ascii_lowercase:
                yield char

    def obtener_cadena(n):
        gen = generador_alfabeto()
        return ''.join(next(gen) for _ in range(n))

    return obtener_cadena(max_letters)


if __name__ == '__main__':
    run(0)