# **************
# EL LOBO ACECHA
# **************


def run(farm: list) -> str:
    if farm[-1] == "lobo":
        return "No te quiero ver más por aquí, lobo"

    indice_lobo = farm.index("lobo")
    if indice_lobo < len(farm) - 1:
        return f"Cuidado oveja {len(farm) - indice_lobo - 1}, el lobo te va a comer"



if __name__ == '__main__':
    run(['oveja', 'oveja', 'lobo', 'oveja'])