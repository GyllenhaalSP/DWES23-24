# ********************************
# UNA MÉTRICA PARA CADENA DE TEXTO
# ********************************


def run(text: str) -> int:
    metric = 0
    for i in text:
        if i in 'aeiou':
            metric += 1
    return len(text) * metric


if __name__ == '__main__':
    run('ordenador')
