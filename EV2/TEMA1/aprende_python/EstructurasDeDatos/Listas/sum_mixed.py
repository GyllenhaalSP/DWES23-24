# ****************
# SUMA HETEROGÉNEA
# ****************


def run(items: list) -> int:
    return sum([int(item) for item in items])


if __name__ == '__main__':
    run([1, '2', 3, '4', 5])
