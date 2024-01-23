"""
 By GyllenhaalSP ene 2024 @ https://github.com/GyllenhaalSP.
"""


class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Titulo: [{self.titulo}], Autor: [{self.autor}]"

    def __eq__(self, other):
        return self.titulo == other.titulo and self.autor == other.autor


if __name__ == '__main__':
    libro1 = Libro("El Quijote", "Cervantes")
    libro2 = Libro("El Quijote", "Cervantes")
    libro3 = Libro("El señor de los anillos", "Tolkien")

    print(libro1)
    print(libro2)
    print(libro3)
    print('Tienen el mismo título y autor' if libro1 == libro2 else 'No tienen el mismo título y autor')
    print('Tienen el mismo título y autor' if libro1 == libro3 else 'No tienen el mismo título y autor')
    print('Tienen el mismo título y autor' if libro2 == libro3 else 'No tienen el mismo título y autor')
