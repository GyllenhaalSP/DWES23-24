# ****************
# SUMANDO MATRICES
# ****************
import filecmp
from pathlib import Path


def run(matrix1_path: Path, matrix2_path: Path) -> bool:
    result_path = 'data/sum_matrix/result.dat'

    def leer_matriz(ruta_fichero):
        with open(ruta_fichero, 'r') as archivo:
            return [[int(num) for num in linea.split()] for linea in archivo]

    def sumar_matrices(matriz1, matriz2):
        return [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1))] for i in range(len(matriz1))]

    def escribir_matriz(matriz, ruta_salida):
        with open(ruta_salida, 'w') as archivo:
            for fila in matriz:
                archivo.write(' '.join(map(str, fila)) + '\n')

    escribir_matriz(sumar_matrices(leer_matriz(matrix1_path), leer_matriz(matrix2_path)), result_path)

    return filecmp.cmp(result_path, 'data\sum_matrix\.expected', shallow=False)


if __name__ == '__main__':
    run('data/sum_matrix/matrix1.dat', 'data/sum_matrix/matrix2.dat')