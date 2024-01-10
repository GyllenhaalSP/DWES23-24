# *************
# SUMA REPETIDA
# *************


def run(n: int) -> int:
    return n + (int(str(n) + str(n))) + (int(str(n) + str(n) + str(n)))


if __name__ == '__main__':
    run(3)
