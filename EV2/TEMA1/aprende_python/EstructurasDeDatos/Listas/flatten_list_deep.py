# ***************
# APLANA LA LISTA
# ***************


def run(elements: list) -> list:
    flattened_list = []
    for element in elements:
        flattened_list.extend(run(element)) if isinstance(element, list) else flattened_list.append(element)

    return flattened_list


if __name__ == '__main__':
    run([0, 10, [20, [-10, [5, 5, 5], -20], 30], 40, 50, [60, 70, [-1, -2, -3], 80], [90, 100, 110, 120]])