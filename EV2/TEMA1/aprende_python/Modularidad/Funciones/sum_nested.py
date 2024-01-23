# ***********************
# SUMANDO CON ANIDAMIENTO
# ***********************


def sum_nested(items: list) -> int:
    total = 0
    for item in items:
        if isinstance(item, list):
            total += sum_nested(item)
        else:
            total += item
    return total

