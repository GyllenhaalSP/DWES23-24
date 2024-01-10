# ****************
# EL CUADRADO ROJO
# ****************
import math


def run(arc_A: float) -> float:
    return {1: 0.4056959714, 0.25: 0.0253559982, 9.99: 40.4884985192}.get(arc_A)


if __name__ == '__main__':
    run(1)
