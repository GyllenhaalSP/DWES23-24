# *********************************
# COMPROBANDO IGUALDAD DE POTENCIAS
# *********************************


def run(n: int) -> tuple:
    left_side = sum([i for i in range(1, n + 1)]) ** 2

    right_side = sum([i ** 3 for i in range(1, n + 1)])

    return left_side, right_side


if __name__ == '__main__':
    run(1)
