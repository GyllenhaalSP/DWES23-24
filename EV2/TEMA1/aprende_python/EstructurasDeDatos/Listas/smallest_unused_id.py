# *****************
# MENOR ID SIN USAR
# *****************


def run(ids: list) -> int:
    ids.sort()
    menor = 1
    for id in ids:
        if id == menor:
            menor += 1
        else:
            break
    return menor


if __name__ == '__main__':
    run([3, 1, 8, 4, 9])