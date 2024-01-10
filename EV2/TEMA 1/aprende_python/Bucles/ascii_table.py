def run() -> str:
    min_ascii = 33
    max_ascii = 128
    ascii_table = ''

    for i in range(min_ascii, max_ascii):
        ascii_table += f'{i:03d} {chr(i)}\t'
        if i % 4 == 0:
            ascii_table += '\n'
    return ascii_table


if __name__ == '__main__':
    print(run())
