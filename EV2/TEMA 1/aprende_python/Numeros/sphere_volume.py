# *********************
# VOLUMEN DE UNA ESFERA
# *********************
import math


def run(radius: float) -> float:
    return 4 / 3 * round(math.pi, 2) * radius ** 3


if __name__ == '__main__':
    run(5)
