# ***************
# UN SET AL TENIS
# ***************


def run(points: str) -> tuple:
    punto1, punto2, juego1, juego2 = 0, 0, 0, 0
    tie_break = False

    for point in points:
        if point == "A":
            punto1 += 1
        else:
            punto2 += 1

        if not tie_break:
            if punto1 >= 4 and (punto1 - punto2) >= 2:
                juego1 += 1
                punto1, punto2 = 0, 0
            elif punto2 >= 4 and (punto2 - punto1) >= 2:
                juego2 += 1
                punto1, punto2 = 0, 0

            if juego1 == 6 and juego2 == 6:
                tie_break = True
        else:
            if (punto1 >= 7 and (punto1 - punto2) >= 2) or (punto2 >= 7 and (punto2 - punto1) >= 2):
                if punto1 > punto2:
                    juego1 += 1
                else:
                    juego2 += 1
                break

    return juego1, juego2


if __name__ == '__main__':
    run('AABBAABABBBABABABBBAAABBBABAABBABBAABBBABABBAAAABBBBABBBAB')
