# **********************
# PIEDRA, PAPEL O TIJERA
# **********************


def run(choice1: str, choice2: str) -> int:
    choices = {
        "piedra": "tijera",
        "papel": "piedra",
        "tijera": "papel",
    }
    c1 = choice1.lower()
    c2 = choice2.lower()

    if c1 == c2:
        return 0
    elif choices[c1] == c2:
        return 1
    else:
        return 2


if __name__ == '__main__':
    run('piedra', 'PAPEL')
