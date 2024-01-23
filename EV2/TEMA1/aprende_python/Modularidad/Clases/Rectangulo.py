"""
 By GyllenhaalSP ene 2024 @ https://github.com/GyllenhaalSP.
"""


class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

    def perimetro(self):
        return (self.largo + self.ancho) * 2


if __name__ == '__main__':
    rectangulo = Rectangulo(10, 5)
    print(f"El área es: {rectangulo.area()}")
    print(f'El perímetro es: {rectangulo.perimetro()}')
    rectangulo.largo = 20
    rectangulo.ancho = 10
    print(f"El área es: {rectangulo.area()}")
    print(f'El perímetro es: {rectangulo.perimetro()}')