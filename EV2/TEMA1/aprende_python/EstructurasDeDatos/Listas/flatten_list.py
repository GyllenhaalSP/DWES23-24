# ***************
# APLANA LA LISTA
# ***************


def run(elements: list) -> list:
    return [element for sublist in elements for element in (sublist if isinstance(sublist, list) else [sublist])]


if __name__ == '__main__':
    run([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])
