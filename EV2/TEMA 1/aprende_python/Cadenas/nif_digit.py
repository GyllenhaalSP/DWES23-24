# *************************
# DÍGITO DE CONTROL DEL NIF
# *************************


def run(nif: str) -> str:
    num = int(nif)
    letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
    return ''.join([nif, letras[(num % 23)]])


if __name__ == '__main__':
    run('78654355')
