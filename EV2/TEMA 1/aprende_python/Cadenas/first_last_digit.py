# ****************************************
# ENCONTRANDO EL PRIMER Y EL ÚLTIMO DÍGITO
# ****************************************


def run(text: str) -> tuple:
    first_digit = ''
    last_digit = ''
    for char in text:
        if char.isdigit():
            first_digit = char
            break

    for char in text[::-1]:
        if char.isdigit():
            last_digit = char
            break
    return int(first_digit), int(last_digit)


if __name__ == '__main__':
    run('1abc2')
