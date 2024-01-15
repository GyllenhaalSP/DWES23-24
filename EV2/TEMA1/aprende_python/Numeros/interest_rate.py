# *****************
# INTERÉS COMPUESTO
# *****************


def run(amount: float, rate: float, years: int) -> float:
    return amount * (1 + rate / 100) ** years


if __name__ == '__main__':
    run(10000, 3.5, 7)
