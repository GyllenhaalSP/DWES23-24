# ***************
# MEZCLA ORDENADA
# ***************


def run(values1: list, values2: list) -> list:
    values = list(set(values1 + values2))
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] > values[j]:
                values[i], values[j] = values[j], values[i]
    return values


if __name__ == '__main__':
    run([1, 2, 3, 4], [1, 1, 2, 3, 4, 5])