# **************
# SUMA INVERTIDA
# **************


def run(numbers: list) -> int:
    return sum([-num for num in numbers])


if __name__ == '__main__':
    run([1, 2, 3, 4, 5])