# **********************
# FRECUENCIA DE PALABRAS
# **********************
from pathlib import Path


def run(input_path: Path, lower_bound: int) -> dict:
    frecuencias = {}
    with open(input_path, 'r') as archivo:
        for linea in archivo:
            palabras = linea.lower().split()
            for palabra in palabras:
                frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    return {palabra: frec for palabra, frec in frecuencias.items() if frec >= lower_bound}


if __name__ == '__main__':
    run('data/word_freq/cistercian.txt', 9)