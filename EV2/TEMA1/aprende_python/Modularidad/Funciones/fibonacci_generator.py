# *******************
# FIBONACCI GENERADOR
# *******************


def run(n: int) -> list:
    def generator(num: int):
        a, b = 0, 1
        for _ in range(num):
            yield a
            a, b = b, a + b

    return list(generator(n))

