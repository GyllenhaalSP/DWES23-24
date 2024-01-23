"""
 By GyllenhaalSP ene 2024 @ https://github.com/GyllenhaalSP.
"""


class Libro:
    def __init__(self, titulo, autor, year):
        self.titulo = titulo
        self.autor = autor
        self.year = year


if __name__ == '__main__':
    libro1 = Libro("El Quijote", "Cervantes", 1615)
    print(libro1.titulo)
    print(libro1.autor)
    print(libro1.year)
