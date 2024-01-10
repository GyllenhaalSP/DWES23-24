# ********************
# MÁXIMO COMÚN DIVISOR
# ********************


def run(a: int, b: int) -> int:
    gcd_value = 1
    for i in range(1, b):
        if a % i == 0 and b % i == 0:
            gcd_value = i

    return gcd_value


if __name__ == '__main__':
    run(1, 1)
