# **********
# HISTOGRAMA
# **********
import filecmp
from pathlib import Path


def run(data_path: Path) -> bool:
    histogram_path = 'data/histogram/histogram.txt'
    char_dict = {}
    with open(data_path, 'r') as data_file:
        for line in data_file:
            for char in line:
                if char in char_dict:
                    char_dict[char] += 1
                else:
                    char_dict[char] = 1

    char_dict = {key: char_dict[key] for key in sorted(char_dict.keys())}

    with open(histogram_path, 'w', encoding="utf8") as histogram_file:
        for char, count in char_dict.items():
            histogram_file.write(f'{char} {"█" * count} {count}\n')

    return filecmp.cmp(histogram_path, 'data\histogram\.expected', shallow=False)


if __name__ == '__main__':
    run('data/histogram/data.txt')