# *****************
# ORDENANDO NÚMEROS
# *****************


def run(numbers: list) -> list:
    lst = numbers[:]
    lst.sort()
    return lst


if __name__ == '__main__':
    run([4, 2, 9, 7, 1, 8])