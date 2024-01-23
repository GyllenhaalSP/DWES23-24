"""
 By GyllenhaalSP ene 2024 @ https://github.com/GyllenhaalSP.
"""


class Circulo:
    def __init__(self, radio):
        self.radio = radio


if __name__ == '__main__':
    circulo = Circulo(5)
    print(circulo.radio)
    circulo.radio = 10
    print(circulo.radio)