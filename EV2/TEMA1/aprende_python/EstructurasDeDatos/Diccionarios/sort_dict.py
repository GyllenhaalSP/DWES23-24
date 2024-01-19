# *********************
# ORDENE MI DICCIONARIO
# *********************


def run(unsorted_items: dict) -> list:
    def valores(x):
        return x[1]
    return sorted(unsorted_items.items(), key=valores)


if __name__ == '__main__':
    run({'a': 'two', 'b': 'one', 'c': 'three'})