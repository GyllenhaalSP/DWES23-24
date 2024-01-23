# ********************
# LEYENDO FICHEROS CSV
# ********************
import csv
from pathlib import Path


def run(datafile: Path) -> list:
    lista_diccionarios = []

    def convertir_valor(valor):
        if valor.isdigit():
            return int(valor)
        if valor in ['True', 'False']:
            return valor == 'True'
        return valor

    with open(datafile, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            diccionario = {clave: convertir_valor(valor) for clave, valor in fila.items()}
            lista_diccionarios.append(diccionario)
    return lista_diccionarios


if __name__ == '__main__':
    run('data/read_csv/pokemon.csv')