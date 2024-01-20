# *******************************
# CONTANDO VOCALES (EN RECURSIVO)
# *******************************


def count_vowels(text: str) -> int:
    vowels = "aeiou"
    if text == "":
        return 0
    elif text[0] in vowels:
        return 1 + count_vowels(text[1:])
    else:
        return count_vowels(text[1:])

