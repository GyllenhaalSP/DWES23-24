# *****************
# DECIMAL A BINARIO
# *****************


def run(num: int) -> str:
    if num == 0:
        return "0"
    binario = ""
    while num > 0:
        resto = num % 2
        binario = str(resto) + binario
        num = num // 2
    return binario


if __name__ == '__main__':
    run(1)
