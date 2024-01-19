# *************************
# MOVIMIENTOS DE INVENTARIO
# *************************


def run(imoves: str) -> dict:
    movimientos = imoves.split(',')
    inventario = {}
    for movimiento in movimientos:
        articulo = movimiento[0]

        if articulo in inventario:
            inventario[articulo] += int(movimiento[1:])
        else:
            inventario[articulo] = int(movimiento[1:])

    return inventario


if __name__ == '__main__':
    run('A1,B4,A-2,A7,B1,C4')