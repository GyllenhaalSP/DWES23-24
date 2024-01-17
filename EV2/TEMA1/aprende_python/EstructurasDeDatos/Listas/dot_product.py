# ****************
# PRODUCTO ESCALAR
# ****************


def run(vector1: list, vector2: list) -> float | None:
    if len(vector1) != len(vector2):
        return None
    return sum([vector1[i] * vector2[i] for i in range(len(vector1))])


if __name__ == '__main__':
    run([4, 3, 8, 1], [9, 2, 7, 3])
