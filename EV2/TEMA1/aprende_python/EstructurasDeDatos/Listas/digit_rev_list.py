# ************************
# DÍGITOS EN ORDEN INVERSO
# ************************


def run(number: int) -> list:
    return [int(number) for number in str(number)[::-1]]


if __name__ == '__main__':
    run(35231)