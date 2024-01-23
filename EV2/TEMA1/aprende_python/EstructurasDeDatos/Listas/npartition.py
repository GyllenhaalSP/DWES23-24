# ***********************
# PARTICIÓN POR EL NÚMERO
# ***********************


def run(values: list, ref_value: int) -> list:
    return [[value for value in values if value < ref_value],
            [value for value in values if value >= ref_value]]


if __name__ == '__main__':
    run([4, 3, 2, 9, 8, 5], 4)