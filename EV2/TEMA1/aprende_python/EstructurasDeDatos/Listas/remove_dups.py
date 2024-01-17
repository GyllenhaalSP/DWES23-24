# *********************
# ELIMINANDO DUPLICADOS
# *********************


def run(nums_dups: list) -> list:
    return list(dict.fromkeys(nums_dups).keys())


if __name__ == '__main__':
    run([2, 3, 2, 2, 1, 5, 4, 2, 4, 9])
