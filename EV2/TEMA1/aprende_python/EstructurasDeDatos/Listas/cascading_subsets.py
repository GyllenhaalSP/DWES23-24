# ***********************
# SUBCONJUNTOS EN CASCADA
# ***********************

def run(values: list, size: int) -> list:
    return list(map(lambda x: values[x:x+size], range(len(values) - size + 1)))


if __name__ == '__main__':
    run([1, 2, 3, 4], 3)