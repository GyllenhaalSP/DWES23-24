# **************************
# BUSCANDO EL SIGLO ADECUADO
# **************************


def run(year: int) -> int:
    return year // 100 + 1 if year % 100 != 0 else year // 100


if __name__ == '__main__':
    run(1705)
