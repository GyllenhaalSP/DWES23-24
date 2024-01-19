# *******************
# CONSONANTES COMUNES
# *******************


def run(text1: str, text2: str) -> str:
    vocales = 'aeiou'
    return ''.join(
        sorted(
            {letra for letra in text1.lower().replace(" ", "") if letra not in vocales}.intersection(
                {letra for letra in text2.lower().replace(" ", "") if letra not in vocales})
        )
    )


if __name__ == '__main__':
    run('Flat is bEtter than nested', 'Readability counts')