# *****************************
# SOMOS IGUALES, PERO DISTINTOS
# *****************************


def run(items: list) -> bool:
    return True if len(set(items)) == 1 else False


if __name__ == '__main__':
    run([1, 1, 1, 1, 1, 1])
