# ********************
# DESCIFRANDO CIUDADES
# ********************


def run(cinfo: str) -> dict:
    cities = [city.split(':')[0] for city in cinfo.split(';')]
    populations = [int(city.split(':')[1]) for city in cinfo.split(';')]
    return dict(zip(cities, populations))


if __name__ == '__main__':
    run('Tokyo:38_140_000;Delhi:26_454_000;Shanghai:24_484_000;Mumbai:21_357_000')
