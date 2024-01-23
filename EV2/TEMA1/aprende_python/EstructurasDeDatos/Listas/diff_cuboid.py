# ********************
# CUBOIDES Y VOLÚMENES
# ********************


def run(cuboid1: list, cuboid2: list) -> float:
    cubo1 = (lambda x, y, z: x * y * z)(*cuboid1)
    cubo2 = (lambda x, y, z: x * y * z)(*cuboid2)
    return abs(cubo1 - cubo2)


if __name__ == '__main__':
    run([2, 2, 3], [5, 4, 1])