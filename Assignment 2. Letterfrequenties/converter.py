from helper import *


def convert(input_file, output_file):      
    lines = []
    with open(input_file, 'r', encoding='utf8') as reader:
        for line in reader:
            splitted = line.strip().split('/')
            lines.append(splitted[0] + '\n')

    with open(output_file, 'w+', encoding='utf8') as writer:
        writer.writelines(lines)


for language in languages:
    convert(f'train_data/{language}.txt', f'train_data/{language}_converted.txt')
