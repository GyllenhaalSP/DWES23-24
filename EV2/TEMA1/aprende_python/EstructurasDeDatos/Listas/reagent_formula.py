# ************
# ELLA QUÍMICA
# ************


def run(formula: list) -> bool:
    if 1 in formula and 2 in formula:
        return False
    if 3 in formula and 4 in formula:
        return False
    if not (5 in formula and 6 in formula) and (5 in formula or 6 in formula):
        return False
    if not (7 in formula or 8 in formula):
        return False

    return True


if __name__ == '__main__':
    run([1, 3, 7])