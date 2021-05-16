import sys
from helper import *


def add_count(left_index, right_index, language_count, matrices):
    key = ''
    for i in range(len(languages) - 1):
        key = languages[i] if matrices[languages[i]][left_index][right_index] >= matrices[languages[i + 1]][left_index][right_index] else languages[i + 1]
    language_count[key] += 1


def map_language(row, line, matrices):
    language_count = { language: 0 for language in languages }
    run_every_word(line, add_count, language_count, matrices)
    language = max(language_count, key=language_count.get)
    print(f'{row}\t{language}')


matrices = get_matrices()
for row, line in enumerate(sys.stdin):
    line = line.strip()
    map_language(row, line, matrices)
