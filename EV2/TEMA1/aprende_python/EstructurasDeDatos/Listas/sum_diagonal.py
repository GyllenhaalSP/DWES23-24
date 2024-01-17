# *****************************
# SUMA DE LA DIAGONAL PRINCIPAL
# *****************************


def run(matrix: list) -> int | None:
    if len(matrix) != len(matrix[0]):
        return None

    return sum([matrix[i][i] for i in range(len(matrix))])


if __name__ == '__main__':
    run([[4, 6, 1], [2, 9, 3], [1, 7, 7]])
