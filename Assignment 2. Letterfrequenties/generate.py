import sys
from helper import *
import csv


# Runned at every letter pair to keep track of the amount of combinations
def add_count(left_index, right_index):
    matrix[left_index][right_index] += 1


# Opening the train data and counting the occurences
def generate_matrix(matrix, language):
    for line in open(f'train_data/{language}_converted.txt', 'r', encoding='utf8'):
        line = line.strip()
        run_every_pair(line, add_count)


# Saving the 2d list in a csv format
def save_matrix(matrix, language):
    with open(f'matrices/{language}_matrix.csv', 'w+', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(matrix)


# Looping trough all the languages and generate and save the matrices
for language in languages:
    matrix = [[0 for col in range(len(letters))] for row in range(len(letters))]
    generate_matrix(matrix, language)
    save_matrix(matrix, language)
