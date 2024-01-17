# ********************
# REORGANIZANDO FECHAS
# ********************


def run(input_date: str, base_year: int) -> str:
    fecha = input_date.split('/')
    base_year_first_two_digits = str(base_year)[:2]
    dia = fecha[1] if len(fecha[1]) > 1 else '0' + fecha[1]
    mes = fecha[0] if len(fecha[0]) > 1 else '0' + fecha[0]
    year = fecha[2] if len(fecha[2]) > 1 else '0' + fecha[2]
    output_date = dia + '-' + mes + '-' + base_year_first_two_digits + year
    return output_date


if __name__ == '__main__':
    run('12/31/23', 2000)
