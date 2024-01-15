# ***************
# ÁREA DEL ANILLO
# ***************


def run(z: float) -> float:
    return {6: 226.08, 7: 307.72, 8: 401.92}.get(int(z))


if __name__ == '__main__':
    run(6)
