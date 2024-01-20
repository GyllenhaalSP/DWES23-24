# *********************************
# SEPARANDO MAYÚSCULAS Y MINÚSCULAS
# *********************************


def split_case(words: list) -> list | tuple:
    return [word for word in words if word.islower()], [word for word in words if word.isupper()]

