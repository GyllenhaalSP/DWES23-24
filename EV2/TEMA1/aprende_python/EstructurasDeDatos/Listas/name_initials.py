# **********************
# INICIALES DE UN NOMBRE
# **********************


def run(fullname: str) -> str:
    nombre = fullname.split(', ')
    apellidos = nombre[0].split(' ')

    return nombre[1][0].upper() + '.' + apellidos[0][0].upper() + '.' + (apellidos[1][0].upper() + '.' if len(
        apellidos) > 1 else '')


if __name__ == '__main__':
    run('Delgado Quintero, sergio')
