# ************************************
# FRECUENCIA DE ELEMENTOS CONSECUTIVOS
# ************************************


def cfreq(items: list, as_string: bool = False) -> list or str:
    resultado = []
    string = ''
    item_actual = items[0]
    counter = 1

    if not items:
        return resultado if not as_string else string

    for item in items[1:]:
        if item == item_actual:
            counter += 1
        else:
            resultado.append((item_actual, counter))
            item_actual = item
            counter = 1

    resultado.append((item_actual, counter))

    return ','.join([f"{item}:{counter}" for item, counter in resultado]) if as_string else resultado
