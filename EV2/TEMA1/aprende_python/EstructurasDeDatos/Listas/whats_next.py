# *********************
# ¿QUÉ ES LO SIGUIENTE?
# *********************


def run(items: list, ref_item: object) -> object:
    if ref_item in items:
        index = items.index(ref_item)
        if index < len(items) - 1:
            return items[index + 1]
    return None


if __name__ == '__main__':
    run([1, 2, 3, 4, 5, 6, 7], 3)