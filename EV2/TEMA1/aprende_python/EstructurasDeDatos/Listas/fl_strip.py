# ****************
# TROCEADO EXTREMO
# ****************


def run(numbers: str) -> str:
    return f'{" ".join(numbers.split(',')[1:-1])}'


if __name__ == '__main__':
    run('1,2,3')