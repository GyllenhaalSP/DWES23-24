# *************************
# NO ME INTERESAN LOS PARES
# *************************


def run(items: list) -> list:
    return [item for index, item in enumerate(items, start=1) if index % 2 != 0]


if __name__ == '__main__':
    run([1, 2, 1, 2, 1, 2])