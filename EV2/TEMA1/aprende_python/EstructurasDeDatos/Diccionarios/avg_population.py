# ******************
# POBLACIÓN PROMEDIO
# ******************


def run(pdata: dict) -> dict:
    return {ciudad: round((poblacion / sum(pdata.values())) * 100, 3) for ciudad, poblacion in pdata.items()}


if __name__ == '__main__':
    run({'Tokyo': 38140000, 'Delhi': 26454000, 'Shanghai': 24484000, 'Mumbai': 21357000})