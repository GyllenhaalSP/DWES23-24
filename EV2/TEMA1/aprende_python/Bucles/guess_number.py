"""
 By GyllenhaalSP ene 2024 @ https://github.com/GyllenhaalSP.
"""
import random

if __name__ == "__main__":
    rand_number = random.randint(1, 100)
    while True:
        number = int(input("Introduce un número: "))
        if number < rand_number:
            print("El número es menor.")
        elif number > rand_number:
            print("El número es mayor.")
        else:
            print("¡Has acertado!")
            break
