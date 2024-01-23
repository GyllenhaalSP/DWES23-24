# *******************
# DE TEXTO A MARKDOWN
# *******************
import filecmp
from pathlib import Path


def run(text_path: Path) -> bool:
    md_path = 'data/txt2md/outline.md'
    with open(text_path, 'r') as file, open(md_path, 'w') as markdown_file:
        for linea in file:
            profundidad = linea.count('\t')
            titulo = linea.strip()
            markdown = '#' * (profundidad + 1) + ' ' + titulo
            markdown_file.write(markdown + '\n')
    return filecmp.cmp(md_path, 'data\\txt2md\.expected', shallow=False)


if __name__ == '__main__':
    run('data/txt2md/outline.txt')