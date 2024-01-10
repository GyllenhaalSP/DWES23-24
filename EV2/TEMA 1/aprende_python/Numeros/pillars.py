# **********************
# POSTES EN LA CARRETERA
# **********************


def run(num_pillars: int, gap_pillars: float, pillar_width: float) -> float:
    return (num_pillars - 1) * (gap_pillars * 100) + (num_pillars - 2) * pillar_width


if __name__ == '__main__':
    run(10, 5, 30)
