# *********************
# PALABRAS CON LONGITUD
# *********************


def run(text: str) -> list:
    return [f"{word} {len(word)}" for word in text.split(" ")]


if __name__ == '__main__':
    run('todo se transforma')