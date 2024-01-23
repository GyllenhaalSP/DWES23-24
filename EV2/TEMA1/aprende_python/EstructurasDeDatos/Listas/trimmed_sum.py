# **************
# SUMA RECORTADA
# **************


def run(values: list) -> int:
    if not values:
        return 0
    max_val = max(values)
    min_val = min(values)
    return sum(v for v in values if v != max_val and v != min_val)


if __name__ == '__main__':
    run([6, 2, 1, 8, 10])