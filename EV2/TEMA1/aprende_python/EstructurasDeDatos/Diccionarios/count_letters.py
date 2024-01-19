# ***************
# CONTANDO LETRAS
# ***************


def run(sentence: str) -> dict:
    counter = {}
    for letra in sentence:
        counter[letra] = counter[letra] + 1 if letra in counter else 1
    return counter


if __name__ == '__main__':
    run('boom')