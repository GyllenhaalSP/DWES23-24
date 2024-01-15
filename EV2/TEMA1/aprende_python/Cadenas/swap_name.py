# ****************
# NOMBRE VICEVERSA
# ****************


def run(fullname: str) -> str:
    name = fullname.split(" ")
    return name[1] + " " + name[2] + " " + name[0] if len(name) > 2 else name[1] + " " + name[0]


if __name__ == '__main__':
    run('John McClane')
