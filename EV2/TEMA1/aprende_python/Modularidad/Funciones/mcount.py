# *******************
# CONTANDO SIN CONTAR
# *******************


def mcount(items: tuple, target: int) -> int:
    """Cuenta el número de veces que aparece un número target en una tupla.

    :param items: Tupla de números.
    :param target: Número target.
    :return: Número de veces que aparece el número target en la tupla.
    """
    return len([i for i in items if i == target])

