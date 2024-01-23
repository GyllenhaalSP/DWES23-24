# **************************************************
# IDENTIFICANDO SECUENCIAS CONSECUTIVAS DE UN TAMAÑO
# **************************************************


def consecutive_seq(items: list, target_count: int) -> int or bool:
    current_count = 1
    if len(items) < target_count:
        return False
    elif target_count == 1:
        return items[0]
    for i in range(len(items) - 1):
        if items[i] == items[i + 1]:
            current_count += 1
            if current_count >= target_count:
                return items[i]
        else:
            current_count = 1
    return consecutive_seq(items[1:], target_count)

