# ***********************
# REEMPLAZO DE CARACTERES
# ***********************
import filecmp
from pathlib import Path


def run(input_path: Path, replacements: str) -> bool:
    output_path = 'data/replace_chars/r_noticia.txt'
    replacements_dict = {rep[0]: rep[1] for rep in replacements.split('|')}

    with open(input_path, 'r', encoding='utf-8') as file:
        content = file.read()
        for old_char, new_char in replacements_dict.items():
            content = content.replace(old_char, new_char)

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)

    return filecmp.cmp(output_path, 'data\\replace_chars\.expected', shallow=False)


if __name__ == '__main__':
    run('data/replace_chars/noticia.txt', 'áa|ée|íi|óo|úu')