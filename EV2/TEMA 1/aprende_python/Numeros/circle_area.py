# ******************
# ÁREA DE UN CÍRCULO
# ******************
import math


def run(radius: float) -> float:
    return round(math.pi, 2) * (radius ** 2)


if __name__ == '__main__':
    run(4)
