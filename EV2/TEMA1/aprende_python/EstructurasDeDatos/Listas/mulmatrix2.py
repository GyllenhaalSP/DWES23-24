# *****************************
# MULTIPLICANDO MATRICES DE 2X2
# *****************************


def run(a: list, b: list) -> list:
    resultado = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                resultado[i][j] += a[i][k] * b[k][j]

    return resultado


if __name__ == '__main__':
    run([[6, 4], [8, 9]], [[3, 2], [1, 7]])
