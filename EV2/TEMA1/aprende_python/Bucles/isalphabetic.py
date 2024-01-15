# ******************
# TODO EN ALFABÉTICO
# ******************


def run(text: str) -> bool:
    for char in text:
        if not char.isalpha():
            return False
    return True


if __name__ == '__main__':
    run('hello-world')
