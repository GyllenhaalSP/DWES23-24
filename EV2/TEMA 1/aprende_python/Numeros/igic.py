# ***************
# PRECIO SIN IGIC
# ***************


def run(price_with_igic: float, igic: float) -> float:
    return round(price_with_igic / (1 + igic / 100), 2)


if __name__ == '__main__':
    run(120, 7)
