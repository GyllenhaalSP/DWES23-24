# *********************
# ENCUENTRA LA INTEGRAL
# *********************


def run(symbol: str) -> str:
    primer_digito = int(symbol[0:symbol.index(',')])
    segundo_digito = int(symbol[symbol.index(',') + 1:len(symbol)])
    exponente = segundo_digito + 1
    primer_termino = primer_digito // exponente
    return str(primer_termino) + 'x^' + str(exponente)


if __name__ == '__main__':
    run('3,2')
