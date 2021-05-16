import sys
from helper import *
import csv


def add_count(left_index, right_index):
    matrix[left_index][right_index] += 1


def generate_matrix(matrix, language):
    for line in open(f'train_data/{language}_converted.txt', 'r', encoding='utf8'):
        line = line.strip()
        run_every_word(line, add_count)


def save_matrix(matrix, language):
    with open(f'matrices/{language}_matrix.csv', 'w+', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(matrix)
        
for language in languages:
    matrix = [[0 for col in range(len(letters))] for row in range(len(letters))]
    generate_matrix(matrix, language)
    save_matrix(matrix, language)
