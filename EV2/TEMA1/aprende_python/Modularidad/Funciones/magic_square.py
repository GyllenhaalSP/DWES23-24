# ***************
# CUADRADO MÁGICO
# ***************


def is_magic_square(values: list):
    n = len(values)
    if n == 0:
        return True

    row_sum = sum(values[0])

    for i in range(n):
        if (sum(values[i]) != row_sum) or (sum(values[j][i] for j in range(n)) != row_sum):
            return False

    return True

