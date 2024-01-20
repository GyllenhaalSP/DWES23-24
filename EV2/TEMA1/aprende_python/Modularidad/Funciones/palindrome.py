# **********
# PALÍNDROMO
# **********


def is_palindrome(text: str) -> bool:
    return text.replace(" ", "").lower() == text[::-1].replace(" ", "").lower()

