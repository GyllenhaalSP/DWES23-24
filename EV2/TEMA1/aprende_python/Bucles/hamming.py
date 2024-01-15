# *****************
# DISTANCIA HAMMING
# *****************


def run(text1: str, text2: str) -> int:
    if len(text1) != len(text2):
        return -1
    acc = 0
    for char1, char2 in zip(text1, text2):
        if char1 != char2:
            acc += 1

    return acc


if __name__ == '__main__':
    run('0001010011101', '0000110010001')
