# **************
# AÑOS BISIESTOS
# **************


def run(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if __name__ == '__main__':
    print(run(1896))
