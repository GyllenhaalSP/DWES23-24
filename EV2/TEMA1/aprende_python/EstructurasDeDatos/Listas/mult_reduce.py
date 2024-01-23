# ************************
# MULTIPLICACIÓN EN CADENA
# ************************
from functools import reduce


def run(numbers: list) -> int:
    return reduce(lambda x, y: x * y, numbers) if len(numbers) > 0 else 1

if __name__ == '__main__':
    run([1, 2, 3, 4])