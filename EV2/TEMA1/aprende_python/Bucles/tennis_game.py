# *****************
# UN JUEGO AL TENIS
# *****************


def run(points: str) -> str:
    a, b = 0, 0
    for point in points:
        if point == "A":
            a += 1
        else:
            b += 1

    if a > b:
        return "A"
    else:
        return "B"


if __name__ == '__main__':
    run('ABAABA')
