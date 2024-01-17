# *********************************
# ELEMENTOS DUPLICADOS CONSECUTIVOS
# *********************************


def run(items: list) -> list:
    return [items[i] for i in range(len(items)) if items[i] != items[i - 1]]


if __name__ == '__main__':
    run([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])
