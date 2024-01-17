# **********************
# DESPLEGANDO CARACTERES
# **********************


def run(texts: list) -> list:
    return [char for word in texts for char in word]


if __name__ == '__main__':
    run(['uno', 'dos', 'tres'])
