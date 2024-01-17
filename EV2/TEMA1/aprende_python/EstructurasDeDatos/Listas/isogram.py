# *********************
# ENCONTRANDO ISOGRAMAS
# *********************


def run(text: str) -> bool:
    for index, char in enumerate(text):
        if char in text[index + 1:] and char not in '-':
            return False
    return True


if __name__ == '__main__':
    run('lumberjacks')
