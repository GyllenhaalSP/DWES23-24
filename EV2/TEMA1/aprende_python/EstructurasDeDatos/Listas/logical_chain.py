# ******************
# CALCULADORA LÓGICA
# ******************


def run(values: list, oper: str) -> bool:
    return all(values) if oper == 'and' else any(values) if oper == 'or' else False


if __name__ == '__main__':
    run([True, True, False], 'and')
