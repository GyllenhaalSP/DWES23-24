# *******************************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO (CON RECURSIVIDAD)
# *******************************************************


def factorial(n: int) -> int or None:
    if n < 0:
        return None
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

