# ********************
# ORDENANDO POR EDADES
# ********************


def run(people: list) -> list:
    return sorted(people, key=lambda person: person['age'])


if __name__ == '__main__':
    run([{'name': 'DeRozan', 'age': 33}, {'name': 'Lonzo', 'age': 25}, {'name': 'Beverly', 'age': 34}, {'name': 'Dragic', 'age': 36}, {'name': 'Williams', 'age': 21}])