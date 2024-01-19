# ********************
# LA CLAVE ES LA CLAVE
# ********************


def run(items: dict) -> dict:
    return {key.replace(" ", ""): value for key, value in items.items()}


if __name__ == '__main__':
    run({'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']})