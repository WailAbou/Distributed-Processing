import string
from sklearn import preprocessing


letters = list(string.ascii_lowercase) + ['_', '?']
languages = ['dutch', 'english']


def print_matrix(matrix):
    matrix.insert(0, letters)
    matrix = [[letters[i - 1]] + row for i, row in enumerate(matrix)]
    cells = lambda row: [str(cell) for cell in row]
    formatted = '\n'.join(['\t'.join(cells(row)) for row in matrix])
    print(formatted, end='\n\n')


def get_index(letter):
    if letter in letters:
        return letters.index(letter)
    else:
        symbol = '_' if letter == ' ' else '?'
        return letters.index(symbol)


def run_every_word(line, action, *args):
    words = line.split()
    for word in words:
        for i in range(len(word) - 1):
            left_word, right_word = word[i], word[i + 1]
            left_index = get_index(left_word)
            right_index = get_index(right_word)
            action(left_index, right_index, *args)


def get_matrix(csv):
    matrix = [[] for row in range(len(letters))]
    for i, line in enumerate(csv.readlines()):
        numbers = list(map(int, line.split(',')))
        matrix[i].extend(numbers)
    return matrix


def get_matrices():
    matrices = {}
    for language in languages:
        csv = open(f'matrices/{language}_matrix.csv', 'r')
        matrix = get_matrix(csv)
        normalized = preprocessing.normalize(matrix)
        matrices[language] = normalized
    return matrices
