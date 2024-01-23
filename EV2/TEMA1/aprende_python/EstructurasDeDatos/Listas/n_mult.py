# ********************
# CALCULANDO MÚLTIPLOS
# ********************


def run(x: int, n: int) -> list:
    return [x * i for i in range(1, n + 1)]


if __name__ == '__main__':
    run(1, 10)