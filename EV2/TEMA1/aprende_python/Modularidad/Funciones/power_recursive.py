# ******************
# POTENCIA RECURSIVA
# ******************


def power(x, n):
    return x * power(x, n - 1) if n > 0 else 1

