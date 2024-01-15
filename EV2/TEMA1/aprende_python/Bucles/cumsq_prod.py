# *******************************
# PRODUCTO ACUMULADO EN CUADRADOS
# *******************************

def run(n: int) -> int:
    acc = 1
    for i in range(1, n + 1):
        acc *= i ** 2

    return int(acc)


if __name__ == '__main__':
    run(4)
