import sys
from helper import *


# Checking which language letter pair is more occuring and setting the line to that
def add_count(left_index, right_index, language_count, matrices):
    key = ''
    for i in range(len(languages) - 1):
        key = languages[i] if matrices[languages[i]][left_index][right_index] >= matrices[languages[i + 1]][left_index][right_index] else languages[i + 1]
    language_count[key] += 1


# Givena a line it will mapp a language to it
def map_language(row, line, matrices):
    language_count = { language: 0 for language in languages }
    run_every_pair(line, add_count, language_count, matrices)
    language = max(language_count, key=language_count.get)
    print(f'{row}\t{language}')


# Loading all matrices
matrices = get_matrices()
#  Enumerating over all the input lines and mapping an language to each line
for row, line in enumerate(sys.stdin):
    line = line.strip()
    map_language(row, line, matrices)
