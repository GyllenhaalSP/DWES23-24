# *******************
# NO ERES CONSECUTIVO
# *******************


def run(values: list) -> int or None:
    for i in range(len(values) - 1):
        if values[i] + 1 != values[i + 1]:
            return values[i + 1]
    return None


if __name__ == '__main__':
    run([1, 2, 3, 4, 6, 7, 8])