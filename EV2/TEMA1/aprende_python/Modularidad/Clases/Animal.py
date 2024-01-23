"""
 By GyllenhaalSP ene 2024 @ https://github.com/GyllenhaalSP.
"""


class Animal:
    def hacer_sonido(self):
        print("Este animal no hace un sonido")


class Perro(Animal):
    def hacer_sonido(self):
        print("Guau!")


if __name__ == '__main__':
    animal = Animal()
    animal.hacer_sonido()
    perro = Perro()
    perro.hacer_sonido()
