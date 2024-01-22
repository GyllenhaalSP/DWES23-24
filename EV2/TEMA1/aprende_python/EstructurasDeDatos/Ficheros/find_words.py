# ***********************************
# ¿DÓNDE ESTÁN LAS PALABRAS? MATARILE
# ***********************************
import re
from pathlib import Path


def run(data_path: Path, target_word: str) -> list:
    ocurrencias = []
    regex = r'\b' + re.escape(target_word) + r'\b'
    with open(data_path, 'r', encoding='utf-8') as archivo:
        for index, linea in enumerate(archivo, start=1):
            for coincidencia in re.finditer(regex, linea, re.I):
                columna = coincidencia.start() + 1
                ocurrencias.append((index, columna))
    return ocurrencias


if __name__ == '__main__':
    run('data/find_words/bzrp.txt', 'persona')