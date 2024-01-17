# **************
# DONANDO SANGRE
# **************


def run(age: int, weight: int, heartbeat: int, platelets: int) -> bool:
    return 18 < age < 65 and weight > 50 and 60 < heartbeat < 100 and platelets > 150000


if __name__ == '__main__':
    run(34, 81, 70, 151000)
