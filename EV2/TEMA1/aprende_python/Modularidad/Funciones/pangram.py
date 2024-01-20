# ********
# PANGRAMA
# ********


def is_pangram(text: str) -> bool:
    return all([letter in text.lower() for letter in "abcdefghijklmnopqrstuvwxyz"])

