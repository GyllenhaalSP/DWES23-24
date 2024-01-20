# ************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO
# ************************************


def factorial(n: int) -> int or None:
    if n < 0:
        return None
    if n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
