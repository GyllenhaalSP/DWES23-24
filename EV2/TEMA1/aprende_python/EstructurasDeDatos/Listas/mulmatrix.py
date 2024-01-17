# **********************
# MULTIPLICANDO MATRICES
# **********************


def run(a: list, b: list) -> list | None:
    if len(a[0]) != len(b):
        return None

    resultado = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                resultado[i][j] += a[i][k] * b[k][j]

    return resultado


if __name__ == '__main__':
    run([[1, 2, 3], [4, 5, 6]], [[5, -1], [1, 0], [-2, 3]])
