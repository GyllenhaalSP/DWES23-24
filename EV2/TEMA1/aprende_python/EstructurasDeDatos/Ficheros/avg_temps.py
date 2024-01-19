# *******************
# TEMPERATURAS MEDIAS
# *******************
import filecmp
from pathlib import Path


def run(input_path: Path) -> bool:
    output_path = 'data/avg_temps/avg_temps.dat'
    with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
        for line in input_file:
            temps = line.replace("\n", "").split(",")
            avg_temp = sum(map(float, temps)) / len(temps)
            output_file.write(f'{avg_temp:.2f}\n')
    return filecmp.cmp(output_path, 'data/avg_temps/.expected', shallow=False)


if __name__ == '__main__':
    run('data/avg_temps/temperatures.dat')
