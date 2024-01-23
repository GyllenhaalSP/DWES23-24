# ********************
# LA PALABRA MÁS LARGA
# ********************
from pathlib import Path


def run(input_path: Path) -> str:
    longest_word = ''
    with open(input_path, 'r') as f:
        for line in f:
            for word in line.split():
                if len(word) >= len(longest_word):
                    longest_word = word
    return longest_word.strip(',.;:()')


if __name__ == '__main__':
    run('data/longest_word/python.txt')