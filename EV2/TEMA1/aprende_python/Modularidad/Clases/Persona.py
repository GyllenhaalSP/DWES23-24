"""
 By GyllenhaalSP ene 2024 @ https://github.com/GyllenhaalSP.
"""


class Persona:
    def __init__(self, edad):
        self.__edad = edad

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        if edad < 0:
            raise ValueError("La edad no puede ser negativa. No se ha modificado")
        self.__edad = edad


if __name__ == '__main__':
    persona = Persona(35)
    print(persona.edad)
    persona.edad = 40
    print(persona.edad)
    try:
        persona.edad = -5
    except ValueError as e:
        print(e)
    print(persona.edad)
