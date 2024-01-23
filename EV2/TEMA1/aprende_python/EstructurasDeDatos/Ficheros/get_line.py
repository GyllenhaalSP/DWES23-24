# *****************
# HAN CANTADO LÍNEA
# *****************
from pathlib import Path


def run(input_path: Path, line_no: int) -> str or None:
    with open (input_path, 'r', encoding='utf-8') as archivo:
        for index, linea in enumerate(archivo, start=1):
            if index == line_no:
                return linea.strip()

    return None


if __name__ == '__main__':
    run('data/get_line/nasdaq.txt', 20)