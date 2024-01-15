# *********************
# CONTANDO MILISEGUNDOS
# *********************


def run(hours: int, minutes: int, seconds: int) -> float:
    return (hours * 3600 + minutes * 60 + seconds) * 1000


if __name__ == '__main__':
    run(0, 1, 1)
