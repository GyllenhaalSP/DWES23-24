# ********************
# DESCUBRIENDO IMPARES
# ********************


def run(values: list) -> list:
    return list(set([value for value in values if value % 2 != 0]))


if __name__ == '__main__':
    run([1, 2, 3, 4, 5])