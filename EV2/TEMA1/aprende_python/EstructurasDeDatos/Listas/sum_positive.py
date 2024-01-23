# **********************
# SUMANDO SOLO POSITIVOS
# **********************


def run(numbers: list) -> int:
    return sum([num for num in numbers if num > 0])


if __name__ == '__main__':
    run([1, -4, 7, 12])